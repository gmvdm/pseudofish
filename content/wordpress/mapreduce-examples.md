Title: MapReduce Examples
Date: 2010-10-30 21:36
Author: gmwils
Category: technology

In investigating [MongoDB][] I decided to explore MapReduce to analyse
the posts from a heap of RSS feeds. However, the MongoDB documentation
is [fairly][] basic. [This post][] has a bit more detail on more complex
map/reduce functions.

Looking outside of MongoDB, there are a few other groups working with
MapReduce. Google started the whole thing off, and has some good
resources:

-   [MapReduce Tutorial][] - good overview of the process with some
    examples.
-   [Original Paper][] - details of the original MapReduce publication
-   [Lecture Series][] - I didn't watch this, but it does seem
    comprehensive.
-   [Slides][] - See Lecture 3.

Some examples of using MapReduce [include][]:

-   **Distributed Grep** - emit(matched line), reduce(identity)
-   **Count of URL Access Frequency** - emit(url, 1), reduce(url, sum)
-   **Reverse Web-Link Graph** - emit(target, source), reduce(target,
    cons) =\> {target, [sources]}
-   **Term-Vector per Host** - {hostname, [term vector]}
-   **Inverted Index**
-   **Distributed Sort**

The reverse web-link graph sounds interesting:

> The map function outputs <target , source> pairs for each link to a
> target URL found in a page named "source". The reduce function
> concatenates the list of all source URLs associated with a given
> target URL and emits the pair:
> </target><target , list(source)>.</target>

There is also [some work][] on using MapReduce to allow for machine
classification to run in parallel. I also found a presentation on [Large
Scale Data Analysis][] that was helpful.

The main thing to get my head around is that the map function can return
more complicated results than just a simple count. The reduce function
then just glues the results together in some way.

And then there is the idea of [multi-pass MapReduce][]. That could get
interesting.

For now, I'm doing a lot of reading. The next step will be start to put
into practice some of these ideas for analysing data. Actually, the next
step is collecting the data, but that's on a different thread.

  [MongoDB]: http://www.mongodb.org/
  [fairly]: http://www.mongodb.org/display/DOCS/MapReduce
  [This post]: http://rickosborne.org/blog/index.php/2010/02/08/playing-around-with-mongodb-and-mapreduce-functions/
  [MapReduce Tutorial]: http://code.google.com/edu/parallel/mapreduce-tutorial.html
  [Original Paper]: http://labs.google.com/papers/mapreduce.html
  [Lecture Series]: http://code.google.com/edu/submissions/mapreduce-minilecture/listing.html
  [Slides]: http://code.google.com/edu/submissions/mapreduce/listing.html
  [include]: http://code.google.com/edu/parallel/mapreduce-tutorial.html#MRExamples
  [some work]: http://atbrox.com/2010/02/08/parallel-machine-learning-for-hadoopmapreduce-a-python-example/
  [Large Scale Data Analysis]: http://www.slideshare.net/marin_dimitrov/large-scale-data-analysis-with-mapreduce-part-i
  [multi-pass MapReduce]: http://cookbook.mongodb.org/patterns/unique_items_map_reduce/
