Title: Following Url Redirects with Clojure
Date: 2010-11-11 00:33
Author: gmwils
Category: Clojure

In attempting to normalize urls for a project, I needed to unravel the
redirects.

Urls that are provided could be via a URL shortening service, an RSS
feed or from another source. To compare them, I need to determine the
final destination of the URL, not what is initially supplied.

To solve this in Clojure, I used the java.net.URL class to open a
connection. By calling .getResponse, the connection will follow through
the redirects. If this is successful, I return the final URL, otherwise
I give back the initial URL.

    :::clojure
    (def test-url "http://feedproxy.google.com/~r/amateurphotographercouk/feeds/rss/newsxml/~3/ds1Q9VsOjhI/story01.htm")
    (defn resolve-redirect [initial-url]
      "Follows any redirects to the supplied url and returns the final destination"
    (let [url (java.net.URL. initial-url)
          conn (.openConnection url)]
      (if (= HttpURLConnection/HTTP_OK (.getResponseCode conn))
        (.. conn getURL toString)
        initial-url)))

I'm still to test this out on a wide variety of production uses, so your
milage may vary.

Note: You'll need to include the HttpURLConnection with
`(:import (java.net HttpURLConnection))` in your namespace declaration.

