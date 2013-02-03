Title: Set the HTTP User-Agent string in Clojure
Date: 2011-04-27 02:38
Author: gmwils
Category: Clojure

I wanted to be able to set the User Agent string for web requests made
from Clojure. This is polite when crawling other sites, otherwise the
request appears as a generic [Java application][].

</p>

To interact with the web, I'm using a [wrapper][] around the Apache http
client.

</p>

To add into your project, put the following in project.clj:

</p>

<p>
    :dependencies  [[clj-http "0.1.2"] ...]

</p>

The user agent string can be set on each call:

</p>
<p>
    (def http-agent "crawlbot/1.0")(defn get-body [url]  (:body (client/get url                     {:headers {"User-Agent" http-agent}})))

</p>

The next step is to move this out to a property that the wrapper can
read, so it can be set once. This refactoring isn't yet justified, as I
make a limited number of calls.

</p>

  [Java application]: http://www.httpuseragent.org/list/Java+VM+1.6-n697.htm
  [wrapper]: https://github.com/getwoven/clj-http
