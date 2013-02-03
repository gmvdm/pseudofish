Title: Installing HAppS
Date: 2006-08-20 14:06
Author: gmwils
Category: Haskell

Update: [HAppS 0.8.2][] is out, which works with the latest version of
FPS. (FPS 0.8 from latest darcs)

HAppS is an application server for Haskell. An initial read of the
[documentation][] makes it seem like a very good platform for building
web applications.

The inspiration for HAppS has come from frameworks such as Python's
twisted, but with the type safety and speed that Haskell can offer.
Initial performance benchmarks look quite promising.

To actually evaluate HAppS, it first needs to be installed. Below is the
list of packages that go together to get it running on Mac OS X Tiger.

### Versions

-   [HAppS][] (from darcs 2006-08-20) - Haskell App Server
-   [FPS][] 0.5 - Fast Packed String library
-   [GHC][] 6.4.1 for Mac OS X - Haskell compiler
-   [Haddock][] 0.7 - Documentation generator
-   [Happy][] 1.15 - Parser generator system
-   [HaXml][] 1.13.1 - XML library
-   [Alex][] 2.0.1 - Lexical analyser generator
-   [cpphs][] 1.2 - Haskell preprocessor

For Haddock to work you will also need a LaTeX system and the DocBook
XSL stylesheets.

### Building

GHC installs as a binary package. The remainder of the packages are
installed using a reasonably standard configure; build; install process.

Haskell has its own build system, based around Cabal files that list
dependencies. Most source packages will include a Setup.hs file and a
\*.Cabal file.

To invoke the Setup.hs file, use either the runhaskell script or make
the Setup.hs file executable (it will then hunt for runhaskell). You
need to have `/usr/local/bin` in your path.

    :::shell
    $ runhaskell ./Setup.hs configure
    $ runhaskell ./Setup.hs build
    $ sudo runhaskell ./Setup.hs install

### FPS

The Fast Packed String library allows for fast string manipulation from
within Haskell. However, there is a bit of a version problem with HAppS.

-   HAppS 0.8 - needs FPS 0.4 (or earlier)
-   HAppS dev - needs FPS 0.5 (0.7 breaks)

FPS changes its interface between minor versions, thus breaking
dependencies for HAppS. It would be good for the HAppS installation to
include the list of versions used to build against, or for FPS to use
better versioning.

### Examples

The example that looks most interesting is [httpd.hs][]. Based on the
behavior of [http://happs.org/][] it appears that they are running this
example as base of the site.

In the examples directory, change the import statement for the
`httpd.hs` file as follows:

    import Data.ByteString.Char8
    --import Data.FastPackedString

Assuming that you are using FPS 0.5 and the development version of
HAppS.

The example can then be run from `examples/` as follows:

    :::shell
    $ make
    $ mkdir HAppS
    $ echo '<h1>Hello World</h1>' > HAppS/README.html
    $ ./httpd

Then point Safari to [http://localhost:5000/][]. The example will
redirect to the file created above and serve the page.

  [HAppS 0.8.2]: http://article.gmane.org/gmane.comp.lang.haskell.general/14292/
  [documentation]: http://happs.org/HAppS/README.html
  [HAppS]: http://happs.org/HAppS/README.html#download
  [FPS]: http://www.cse.unsw.edu.au/~dons/fps.html
  [GHC]: http://www.haskell.org/ghc/download_ghc_641.html#macosx
  [Haddock]: http://haskell.org/haddock/#Download
  [Happy]: http://www.haskell.org/happy/#download
  [HaXml]: http://www.cs.york.ac.uk/fp/HaXml
  [Alex]: http://www.haskell.org/alex/#Download
  [cpphs]: http://www.cs.york.ac.uk/fp/cpphs/
  [httpd.hs]: http://happs.org/HAppS/examples/httpd.hs
  [http://happs.org/]: http://happs.org/
  [http://localhost:5000/]: http://localhost:5000/
