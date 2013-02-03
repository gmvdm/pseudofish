Title: Bitly API via Clojure
Date: 2011-07-03 04:51
Author: gmwils
Category: Clojure

While playing with links in Clojure for [Photozeit][], I wanted to
shorten them via Bit.ly and to also lookup click counts per link.

The API is quite straightforward, so I wrote a small library,
[clojure-bitly][], to allow access to it from Clojure.

The Github page includes some example code, and the library can be
downloaded from [Clojars][] using either Lein or Maven.

Here is how to shorten a url:

    :::clojure
    user> (bitly/with-auth *bitly-user* *bitly-apikey*
            (bitly/shorten "http://www.google.com/"))
    "http://j.mp/lMfE5t"
    user>

The [Bitly API docs][] have more details on which methods are available,
or check out the [source][].


  [Photozeit]: http://www.photozeit.org/
  [clojure-bitly]: https://github.com/gmwils/clojure-bitly
  [Clojars]: http://clojars.org/clojure-bitly
  [Bitly API docs]: http://code.google.com/p/bitly-api/wiki/ApiDocumentation#/v3
  [source]: https://github.com/gmwils/clojure-bitly/blob/master/src/bitly.clj
