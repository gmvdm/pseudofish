Title: Genetic Algorithms in Haskell
Date: 2007-12-16 00:20
Author: gmwils
Category: Haskell, Technology

I started with the idea of playing around with Genetic Algorithms
([GAs][]) in Haskell.The [links][] I found were to two research papers,
not two implementations. Each research paper takes a different approach
to developing a GA library, and includes some code as an example.

The two approaches differ mainly in the representation of the genome for
the GA. The trade-offs are outlined below.

### An Array of Bits

The genome is represented by a bit array `:: (Fitness, [Bool])`. This is
the approach taken by the authors of "[A Genetic Algorithm Framework
Using Haskell][]".

**Advantages**

-   easy expression of GA algorithms

**Disadvantages**

-   challenging to encode/decode problem space to a bit array :: [Bool]

My memory of this from Uni is that we spent lots of time simply
constructing an appropriate representation in a bit array (in C++), and
then building useful fitness functions. The GA framework then did all
the heavy lifting as a black box.

I'd really hope there was a more elegant way of representing the Genome
using general types. In nature, the genome is essentially a giant array
of 2 bit values. GATTACA. However, it takes the entire planet to
calculate the fitness function.

### Type Classes

The genome is represented by a generic type. The basic operators are
then expressed using Haskell type classes. This is the approach taken by
the authors of "[Genetic algorithms in Haskell with polytypic
programming][]"

**Advantages**

-   logical mapping of problem to genome

**Disadvantages**

-   requires polytypic language extensions to generalise algorithms
-   polytypic extension requires additional compilation step
-   current polytypic extension limits haskell features used

The polytypic solution is quite elegant in allowing functions such as
mutate to be written once and apply to many types. That said, it does
introduce some restrictions.

The challenge is to abstract the combinators of Genomes without
requiring polytypic extensions. Otherwise, consumers of the library will
need to write appropriate library functions specific to their types.
This may be more time consuming than mapping the problem space to an
array of bits.

My theory is that a well written GA library should be possible that
caters to the majority cases for data structures without needing to
resort to polytypic extensions. This should allow the consumer of the
library to utilize the full power of Haskell without spending time
writing too much GA specific code.

  [GAs]: http://en.wikipedia.org/wiki/Genetic_algorithm
  [links]: http://haskell.org/haskellwiki/Applications_and_libraries/Genetic_programming
  [A Genetic Algorithm Framework Using Haskell]: http://www.comp.rgu.ac.uk/staff/jm/myPublications.html
  [Genetic algorithms in Haskell with polytypic programming]: http://www.cs.chalmers.se/~patrikj/poly/others/geneticalgorithmsinhaskellwithpolytypicprogramming.ps.gz
