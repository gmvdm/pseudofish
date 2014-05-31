Title: Analysing Skritter time series data with R
Date: 2014-05-31
Author: gmwils
Summary: Using the great time series functions in R, analyse learning data from Skritter usage.

[Skritter](http://www.skritter.com/home) tracks data on my Chinese study while
I use it. With their new [API](http://www.skritter.com/api/v0/docs), I can make use of
[R](http://www.r-project.org/) to try and spot some trends.

With emacs, try out
[ESS mode](http://stats.blogoverflow.com/2011/08/using-emacs-to-work-with-r/). `C-c
C-l` loads the current buffer into an ESS buffer running R.

## Downloading the data

Using a [client](https://github.com/gmwils/skritter) for the Skritter API,
you can download either
[progress stats](http://www.skritter.com/api/v0/docs/endpoints/progress_stats)
or every [item](http://www.skritter.com/api/v0/docs/endpoints/items) you've
ever studied. I chose to start with progress statistics.

The script I used is available
[here](https://github.com/gmwils/skritter/blob/master/examples/progress_stats.py).

There is a lot of data returned across three dimensions:

* word and character level stats
* definition, reading, writing (rune), and tone
* learned, learning, remembered, and studied items

In addition, there is the number of days studied, and the time studied in
seconds. You can request by day, week or month, with different limits.

I wanted as long a timespan as possible, so downloaded two years of data at
month granularity. I then dumped it all into a CSV file, with a header row.

For example:

```
date,client,days studied,time studied,word defn learned,...
2012-05-01,,0,0.0,0,...
2012-06-01,,18,25669.0,...
2012-07-01,,48,57054.0,...
2012-08-01,,79,96913.0,...
```

## Loading into R

Loading the data into R is straightforward.

```r
skritter.raw <- read.csv("data/skritter_stats.csv")
```

The data is now all in one place:

```r
colnames(skritter.raw)
```

```
##  [1] "date"                    "client"                 
##  [3] "days.studied"            "time.studied"           
##  [5] "word.defn.learned"       "word.defn.learning"     
##  [7] "word.defn.remembered"    "word.defn.studied"      
##  [9] "word.reading.learned"    "word.reading.learning"  
## [11] "word.reading.remembered" "word.reading.studied"   
## [13] "word.rune.learned"       "word.rune.learning"     
## [15] "word.rune.remembered"    "word.rune.studied"      
## [17] "word.tone.learned"       "word.tone.learning"     
## [19] "word.tone.remembered"    "word.tone.studied"      
## [21] "char.defn.learned"       "char.defn.learning"     
## [23] "char.defn.remembered"    "char.defn.studied"      
## [25] "char.reading.learned"    "char.reading.learning"  
## [27] "char.reading.remembered" "char.reading.studied"   
## [29] "char.rune.learned"       "char.rune.learning"     
## [31] "char.rune.remembered"    "char.rune.studied"      
## [33] "char.tone.learned"       "char.tone.learning"     
## [35] "char.tone.remembered"    "char.tone.studied"
```

## Cleaning up the data
Given that this is a time series, that is the first transformation to make:

```r
skritter.cumulative <- ts(skritter.raw[, -1], start = c(2012, 5), frequency = 12)
```

The `ts` function converts the data frame into a time series object. I strip
out the first column (`skritter.raw[,-1]`), as the time information is now in
the time series.

Examining a column shows that the data is cumulative:


```r
skritter.cumulative[, "word.tone.remembered"]
```

```
##        Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep   Oct   Nov
## 2012                             0   269   776  1368  2322  3357  4161
## 2013  5838  6480  7136  8455  9490 10844 12310 13954 16252 18175 20265
## 2014 23703 25574 27319 28972 30694                                    
##        Dec
## 2012  5226
## 2013 22002
## 2014
```

To get the increment per month, we can subtract the time series from itself
with a lag introduced. Time series in R use different functions than data
frames, so double check you still have a time series (eg. `is.ts(...)`).


```r
skritter <- diff(skritter.cumulative, lag = 1, difference = 1)
skritter[, "word.tone.remembered"]
```

```
##       Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
## 2012                           269  507  592  954 1035  804 1065
## 2013  612  642  656 1319 1035 1354 1466 1644 2298 1923 2090 1737
## 2014 1701 1871 1745 1653 1722
```

```r
is.ts(skritter)
```

```
## [1] TRUE
```

Now all the columns show the increase (or decrease) per month, while remaining
a time series.

## Visualising trends

The actual numbers aren't so interesting, as they correlate to the amount of
time spent.

To see the relationship between two series, try:


```r
plot(days.studied ~ word.rune.remembered, data = skritter)
```

![plot of chunk days_studied](|filename|/images/days_studied.png) 

However, the number of days isn't as useful as the actual time spent:

```r
plot(time.studied ~ word.rune.remembered, data = skritter)
```

![plot of chunk time_studied](|filename|/images/time_studied.png) 

The next thing is to compare the ratios between time spent and aspects of
studying. To simplify, I used a function to extract parts of the data:

```r
extractsummary <- function(s, aspect = "remembered", type = "word") {
    summary <- ts.union(reading = s[, paste(type, "reading", aspect, sep = ".")], 
        tone = s[, paste(type, "tone", aspect, sep = ".")], rune = s[, paste(type, 
            "rune", aspect, sep = ".")], defn = s[, paste(type, "defn", aspect, 
            sep = ".")])
    return(summary)
}
```

`paste` is used to construct the column names:

```r
paste("word", "reading", "remembered", sep=".")
```

```
## [1] "word.reading.remembered"
```

And grabbed data for both words and characters remembered:

```r
word.remembered <- extractsummary(skritter)
char.remembered <- extractsummary(skritter, type = "char")
```

R can operate across all the columns at the same time. This
makes it easy to plot the number of character aspects remembered
per hour of study.

The column names need to be re-added, so they show as plot labels.

```r
char.remembered.per.hour <- (char.remembered * 60 * 60)/skritter[, "time.studied"]
colnames(char.remembered.per.hour) <- colnames(char.remembered)
plot(char.remembered.per.hour, main = "Character aspects remembered per hour")
```

![plot of characters remembered per hour](|filename|/images/chars_per_hour.png) 

Looking at the plot, I seem to be improving the number of tones that I
learn per hour, and slightly improving on how fast I learn new writings. Definitions
and reading seem to have taken about the same time across two years.

Repeating for words:

```r
word.remembered.per.hour <- (word.remembered * 60 * 60)/skritter[, "time.studied"]
colnames(word.remembered.per.hour) <- colnames(word.remembered)
plot(word.remembered.per.hour, main = "Word aspects remembered per hour")
```

![plot of words rememberd per hour](|filename|/images/word_per_hour.png) 


There are a few other plots that are useful.

For example, looking at the words learned by season:

```r
seasonplot(skritter[, "word.tone.learned"])
```

![seasonplot of word tones learned](|filename|/images/seasonal1.png)

```r
monthplot(skritter[, "word.tone.learned"])
```

![monthplot of word tones learned](|filename|/images/seasonal2.png)


Looking at these, I seem to put more time into Chinese study during August,
September and October.

## Further reading

These articles and PDFs helped me understand how and why time series in R are
useful:

* [Forecasting: principles and practice](https://www.otexts.org/fpp) -- there
  is so much in this free online book.
* [Fpp - Using R](https://www.otexts.org/fpp/using-r) -- crash course in time
  series for R.
* [Introduction to R's time series facilities](http://people.su.se/~lundh/reproduce/introduction_ts.pdf)
  -- an ebook, helpful for converting mathematical functions to R time series.

To generate this post, I used [RMarkdown](http://kbroman.github.io/knitr_knutshell/pages/Rmarkdown.html).
