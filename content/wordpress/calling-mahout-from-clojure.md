Title: Calling Mahout from Clojure
Date: 2011-08-18 18:07
Author: gmwils
Category: technology

Mahout is a set of libraries for running machine learning processes,
such as recommendation, clustering and categorisation.

The libraries work against an abstract model that can be anything from a
file to a full Hadoop cluster. This means you can start playing around
with small data sets in files, a local database, a Hadoop cluster or a
custom data store.

After a bit of [research][], it turned out not to be too complex to call
via any JVM language. When you compile and install Mahout, the libraries
are installed into your local Maven cache. This makes it very easy to
include them into any JVM type project.

To help work through the various features, I'm reading the early access
edition of [Mahout in Action][]. I am trying out the [examples][] in
Clojure as I read through.

To get started, the following steps will setup a Clojure project to work
with Mahout:

1.  [Build and install Mahout][]

    The process installs the Mahout jars into your local maven
    repository, making them accessible to lein.

2.  Create a new project

        lein new mahoutexample

3.  Add dependencies to [project.clj][].

    For example:

        :dependencies [
          [org.clojure/clojure "1.2.1"]
          [org.apache.mahout/mahout-core "0.5"]
          [org.apache.mahout/mahout-math "0.5"]
          [org.apache.mahout/mahout-utils "0.5"]]

    Then load the dependencies into your project:

        lein deps

4.  Add your code

    For example, [ch02.clj][] shows calling a recommendation engine.

    The time consuming part is adding in the right import statements.

5.  Evaluate from the REPL

    This is where it gets fun. Clojure makes it easy to try out
    different data sets and learning algorithms to rapidly iterate.

6.  [Optional] Add a run task

    In [project.clj][], you can assign a class as the main class. Lein
    will attempt to find a function called "[-main][]" and call that.

        lein run


As an example, I've ported the first chapter of the book to Clojure and
it is available on [github][].

Some other articles on using parts of Mahout with Clojure are the *opus
artificem probat* blog:

-   [Visualizing Mahout’s output with Clojure and Incanter][]
-   [Monte Carlo integration with Clojure and Mahout][]

  [research]: http://groups.google.com/group/clojure/browse_thread/thread/6e01fd108c32d701?pli=1
  [Mahout in Action]: http://www.manning.com/owen/
  [examples]: http://www.manning.com/owen/MIA_Recommender_code_archive.zip
  [Build and install Mahout]: https://cwiki.apache.org/MAHOUT/buildingmahout.html
  [project.clj]: https://github.com/gmwils/mahoutinaction/blob/master/project.clj
  [ch02.clj]: https://github.com/gmwils/mahoutinaction/blob/master/src/mahoutinaction/ch02.clj
  [-main]: https://github.com/gmwils/mahoutinaction/blob/master/src/mahoutinaction/core.clj#L12
  [github]: https://github.com/gmwils/mahoutinaction
  [Visualizing Mahout’s output with Clojure and Incanter]: http://antoniogarrote.wordpress.com/2011/05/08/visualizing-mahouts-output-with-clojure-and-incanter/
  [Monte Carlo integration with Clojure and Mahout]: http://antoniogarrote.wordpress.com/2011/06/26/monte-carlo-integration-with-clojure-and-mahout/
