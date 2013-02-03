Title: Storm - a real time Hadoop like system in Clojure
Date: 2011-09-26 02:33
Author: gmwils
Category: Clojure

I am very excited about the potential unleashed by [Storm][].

</p>

Previously at BackType, [Nathan Marz][] has now built Storm into Twitter
and then open sourced the platform.

</p>

Storm opens up a lot of possibilities, by bringing real-time distributed
processing together in an elegant way. And it is built in Clojure!

</p>

Some useful links:

</p>

-   [Rationale][]
-   [Slides][] - detailed presentation on Storm by Nathan
-   [Starter project][] - a few basic demo use cases
-   [Mailing List][]
-   [Taking the Emmys by Storm][] - an hour long video of how to use
    Storm to aggregate data from Twitter in realtime to spot trends.

</p>

While playing around I wanted to try from Clojure (most examples are in
Java). There is a great DSL for Clojure that makes using Storm super
easy. I forked the [storm-starter][] project to add [examples][] based
on a [Gist][] from Nathan.

</p>

  [Storm]: https://github.com/nathanmarz/storm
  [Nathan Marz]: https://twitter.com/nathanmarz
  [Rationale]: https://github.com/nathanmarz/storm/wiki/Rationale
  [Slides]: http://www.slideshare.net/nathanmarz/storm-distributed-and-faulttolerant-realtime-computation
  [Starter project]: https://github.com/nathanmarz/storm-starter
  [Mailing List]: http://groups.google.com/group/storm-user
  [Taking the Emmys by Storm]: http://storm.twitsprout.com/
  [storm-starter]: https://github.com/gmwils/storm-starter/
  [examples]: https://github.com/gmwils/storm-starter/blob/master/src/clj/storm/starter/wordcount.clj
  [Gist]: https://gist.github.com/1228302
