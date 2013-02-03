Title: Bits and Pieces of Haskell
Date: 2006-11-28 18:11
Author: gmwils
Category: Haskell

There are a few threads that I've been attempting to unravel that don't
quite justify their own post. However, as each is proving to be very
interesting, I've gathered them together:

-   [Arrows][] - *"Arrows are a new abstract view of computation ...
    [that] serve much the same purpose as monads -- providing a common
    structure for libraries -- but are more general."*

    A monad generalises a computation across its output. An arrow
    generalises computation for both input and output.

    For fun, a Kleisli arrow will lift a monad abstraction to an arrow
    abstraction, but the interesting arrows are the ones that can't be
    made into monads. Essentially, the arrow abstraction is a super-set
    of monadic abstractions.

    If you want to understand the *why* of arrows, read [[Hug00][]]. If
    you want to understand the *how* of arrows, read [[Hug05][Hug00]]

    As usual with Haskell, the interesting bits are in research papers.


-   Software Transactional Memory ([STM][]) - *"a quantum step forward
    from locks and conditionals"* in concurrent programming.

    Simon Peyton-Jones and Tim Harris were recently [interviewed][] by
    Channel 9 on STM. The discussion covers the motivation of STM and
    outlines the types of problems it solves.

    [STM][1] is available today in Haskell, as a GHC extension.


-   [Types and Programming Languages][] - If you have an interest in
    computational theory and type systems, I cannot recommend this book
    enough. [Autrijus][] blamed this book for him starting the [pugs][]
    project.

    I'm only part way through the book, and it is stretching my brain in
    interesting ways. The benefit is that much of the terminology in
    research papers in functional programming is becoming more clear.

    I haven't had this much fun since writing a monadic based lambda
    calculus parser at [uni][].

-   [Category theory][] - this is floating around the edges of a number
    of topics. There are veiled and direct references to how category
    theory is responsible for concepts such as monads and arrows.

    From [[Hug05][Hug00]]:

    > Arrows in Haskell are directly inspired by category theory, which
    > in turn is just the theory of arrows — a category is no more than
    > a collection of arrows with certain properties.

    For now, category theory is on my *"to read"* list, having piqued my
    interest.

To keep up to date with what it happening in the Haskell community, I
highly recommend the [Haskell Weekly Report][] ([rss][]).


  [Arrows]: http://www.haskell.org/arrows/
  [Hug00]: http://www.haskell.org/arrows/biblio.html
  [STM]: http://en.wikipedia.org/wiki/Software_Transactional_Memory
  [interviewed]: http://channel9.msdn.com/Showpost.aspx?postid=231495
  [1]: http://www.haskell.org/ghc/docs/latest/html/libraries/stm/Control-Concurrent-STM.html
  [Types and Programming Languages]: http://www.amazon.com/exec/obidos/asin/0262162091/ref=nosim/pseudofish-20
  [Autrijus]: http://en.wikipedia.org/wiki/Audrey_Tang
  [pugs]: http://en.wikipedia.org/wiki/Pugs
  [uni]: http://www.unimelb.edu.au/HB/subjects/433-431.html
  [Category theory]: http://en.wikipedia.org/wiki/Category_theory
  [Haskell Weekly Report]: http://www.haskell.org/haskellwiki/Haskell_Weekly_News
  [rss]: http://sequence.complete.org/node/feed
