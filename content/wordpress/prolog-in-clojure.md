Title: Prolog in Clojure
Date: 2011-08-05 16:31
Author: gmwils
Category: Clojure

After reading Peter Novig's classic, [Paradigms of AI Programming][], I
decided to try porting his implementation of Prolog in Lisp to Clojure.

</p>

The initial results are available on [GitHub][].

</p>

The interpreter allows solving of simple [logic problems][]:

</p>

<p>
    (<- (witch ?x) (burns ?x) (female ?x))(<- (burns ?x) (wooden ?x))(<- (wooden ?x) (floats ?x))(<- (floats ?x) (sameweight Duck ?x))(<- (female Girl))(<- (sameweight Duck Girl))(?- (witch Girl))

</p>

Porting this turned out to be an interesting challenge. There were a few
Lisp functions that weren't available in Clojure, along with some subtle
changes in idiom.

</p>

This gave me an opportunity to dive further into Clojure and think about
how to implement the algorithms and data structures in a way that made
sense, yet was still close to the original.

</p>

There is still much to do, as the book further develops the interpreter
with user interaction and then refactors it into a compiler. Should keep
me busy for a while longer!

</p>

Note: Please don't consider this production code. If you want to look
deeper at logic programming, consider either a real Prolog
implementation, the [core.logic][] library in Clojure or check out
[Mercury][].

</p>

  [Paradigms of AI Programming]: http://www.amazon.com/gp/product/1558601910/ref=as_li_ss_tl?ie=UTF8&tag=pseudofish-20&linkCode=as2&camp=217145&creative=399369&creativeASIN=1558601910
  [GitHub]: http://github.com/gmwils/clj-prolog
  [logic problems]: http://www.allisons.org/ll/Logic/Prolog/Examples/witch/
  [core.logic]: https://github.com/clojure/core.logic
  [Mercury]: http://www.mercury.csse.unimelb.edu.au/
