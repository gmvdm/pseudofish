Title: Analysis of data with MongoDB and R
Date: 2011-05-25 00:59
Author: gmwils
Category: Technology

For my [photography news][] site, I've ended up with a data store of a
lot of blog articles in [MongoDB][]. To try and look for patterns, I
want to run some analysis. [R][] looks like the right tool for the job.

</p>

### Integration Installation

</p>

To link [R][] to Mongo, use the [RMongo][] library. Behind the scenes,
this uses a R to Java bridge and the Java MongoDB driver.

</p>

Installation is reasonably simple:

</p>

1.  Validate

    </p>
    <p>
        $ cd ..$ R CMD check RMongo

2.  Build

    </p>
    <p>
        $ R CMD build RMongo

3.  Install

    </p>
    <p>
        $ R CMD install RMongo*.tar.gz

</p>

These steps assume you already have R installed and available from the
command line.

</p>

### Query for Data

</p>

Now from within R, you can connect to a local MongoDB. The
mongoDbConnect function takes some additional arguments if your database
is remote.

</p>

<p>
    > library("RMongo")> mongo  < - mongoDbConnect("db")> result < - dbGetQuery(mongo, "items", "", 0, 10)> result$publish_date [1] "2011-03-03" "2011-03-03" "2011-04-20" "2011-01-24" "2011-01-24" "2011-04-11" "2011-03-29" [8] "2011-03-28" "2011-03-22" "2011-03-14"

</p>

To some extent, it is as simple as that. You can use more complex
queries to extract the data that you want.

</p>

The main query function takes five arguments:

</p>

-   database connection
-   collection name
-   query
-   skip - how many objects to skip
-   limit - total number of objects to return

</p>

For example, extract all fields from an items collection where an item
was published during April 2011:

</p>

<p>
    > result < - dbGetQuery(mongo, "items", "{'publish_date' : { '$gte' : '2011-04-01', '$lt' : '2011-05-01'}}")

</p>

To limit data returned to specific fields, use dbGetQueryForKeys
instead:

</p>

<p>
    > result < - dbGetQueryForKeys(mongo, "items", "{'publish_date' : { '$gte' : '2011-04-01', '$lt' : '2011-05-01'}}", "{'publish_date' : 1, 'rank' : 1}")

</p>

### Plotting of Results

</p>

First, summarise the results into a table:

</p>

<p>
    > res < - transform(result, day = weekdays(as.Date(publish_date)))> res.days < - factor(res$day, levels = c('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'), ordered=TRUE)> table(res.days)res.days   Sunday    Monday   Tuesday Wednesday  Thursday    Friday  Saturday        30        74       123       121       131       128        86 > 

</p>

Then, plot as a barchar:

</p>

<p>
    > barplot(t(as.matrix(table(res.days))), main='Items per day of week')

</p>

Which gives the following graphic:

</p>

![Items per day][]

This makes it easy to see how many articles were available per day
across April.

</p>

While I am still scratching the surface, the combination of R with
MongoDB looks to be quite useful.

</p>

  [photography news]: http://photozeit.org/
  [MongoDB]: http://www.mongodb.org/
  [R]: http://www.r-project.org/
  [RMongo]: https://github.com/quid/RMongo
  [Items per day]: /illustrations/2011/items_per_day.png
    "items_per_day.png"
