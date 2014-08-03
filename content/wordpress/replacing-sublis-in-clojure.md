Title: Replacing sublis in Clojure
Date: 2011-07-27 04:06
Author: gmwils
Category: clojure

In porting some Lisp code across to Clojure, I was missing the
[sublis][] function, or at least something similar.

The closest I could find was `replace`, however it failed on nested
structures:

    user> (replace '{?x ?x_123} '(?x (?y ?x)))(?x_123 (?y ?x))

`postwalk-replace` from [clojure.walk][] solved the problem:

    user> (use 'clojure.walk)
    nil
    user> (postwalk-replace '{?x ?x_123} '(?x (?y ?x)))(?x_123 (?y ?x_123))

I almost started to write out my own recursive solution. However, I
thought that walking clojure data should be a solved problem, and found
that replacing elements was also a solved problem.

The more I read through the standard libraries for Clojure, the less
code I write.

  [sublis]: http://www.audacity-forum.de/download/edgar/nyquist/nyquist-doc/xlisp/xlisp-ref/xlisp-ref-267.htm
  [clojure.walk]: http://richhickey.github.com/clojure/clojure.walk-api.html
