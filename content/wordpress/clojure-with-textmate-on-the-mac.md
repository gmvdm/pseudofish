Title: Clojure with TextMate on the Mac
Date: 2010-06-17 21:41
Author: gmwils
Category: Technology

[Clojure][] has been getting a bit of press recently, such as prominence
on the ThoughtWorks [Technology Radar][]. Having spent some time
learning Lisp in the [past][], I thought it could be a good holiday
project to play with.

This post pulls together some of the resources I found for getting
started. I'm not going to try and sell you on a Lisp dialect that
integrates into the JVM, it should be self evident.

### TextMate Setup

[TextMate][] has a [bundle][] that makes it very simple to get started.
It includes the clojure runtime, and so you can run clojure code after
installation. To install (assuming you have git):

    cd ~/Library/Application\ Support/TextMate/Bundles
    git clone git://github.com/nullstyle/clojure-tmbundle.git Clojure.tmbundle
    osascript -e 'tell app "TextMate" to reload bundles'

Then create a folder, open it in TextMate, create a file (ie.
`test.clj`) and put some sample code into it:


    (+ 1 2 3)
    (println "Hello from the console")
    (. javax.swing.JOptionPane (showMessageDialog nil "Hello World"))

Put the cursor into one of the expressions and press Apple-R. TextMate
will figure the rest out and show the result. Apple-Shift-R will run all
the expressions.

(The [Vim][] setup looks really good, but I'm committed to learning
TextMate at the moment)

### Tutorials

I'm not going to be exhaustive on this, but thought I'd include a few
pointers (see also [Alexandre's summary][]). There is a video series
available on [YouTube][], and also on [BlipTV][].

[This][] is an overview in a cheatsheet, and there is a fairly complete
language reference [here][] and a longer [list of references][] as well.

Given that Clojure is Lisp based, it would make sense to understand
Lisp. The best option is a book called [Practical Common Lisp][]. This
is available on the web for free, or can be purchased from Amazon.

**Update:** Apparently I was off a bit on the utility of the Common Lisp
book.

From @[cemerick][]: @[gmwils][] FYI, Clojure is a lisp, but has little
to do with Common Lisp. For books, try [http://bit.ly/ccSw2Z][] or
[http://joyofclojure.com/][]

  [Clojure]: http://clojure.org/getting_started
  [Technology Radar]: http://www.thoughtworks.com/radar/
  [past]: http://pseudofish.com/blog/2007/02/14/lisp-in-a-box/
  [TextMate]: http://macromates.com/
  [bundle]: http://github.com/nullstyle/clojure-tmbundle
  [Vim]: http://www.assembla.com/wiki/show/clojure/Getting_Started_with_Vim
  [Alexandre's summary]: http://alexandrenotebook.blogspot.com/2009/04/starting-up-clojure-simple-tips.html
  [YouTube]: http://www.youtube.com/watch?v=Aoeav_T1ARU&feature=PlayList&p=00D7ACB417C22451&index=0&playnext=1
  [BlipTV]: http://clojure.blip.tv/
  [This]: http://clojure.org/cheatsheet
  [here]: http://java.ociweb.com/mark/clojure/article.html
  [list of references]: http://java.ociweb.com/mark/clojure/
  [Practical Common Lisp]: http://www.gigamonkeys.com/book/
  [cemerick]: https://twitter.com/cemerick/status/16382771631
  [gmwils]: http://twitter.com/gmwils
  [http://bit.ly/ccSw2Z]: http://bit.ly/ccSw2Z
  [http://joyofclojure.com/]: http://joyofclojure.com/
