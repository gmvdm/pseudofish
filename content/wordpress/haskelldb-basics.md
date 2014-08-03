Title: HaskellDB Basics
Date: 2008-05-11 23:35
Author: gmwils
Category: haskell

[HaskellDB][] is a domain specific embedded language for specifying
database queries and operations.

The upside of this is the full Haskell language for writing queries and
the Haskell compiler and type checker for validating database code. The
(big) downside is the error messages are horribly cryptic; although once
is compiles it is likely to be correct.

The original version of HaskellDB was re-written to be more portable and
usable in more situations. Unfortunately, the documentation is out of
step with the current code.

Installation is particularly tricky.

The following is an example query:

    :::haskell
    stockInfo :: Database -> String
                 -> IO [(CompanyName, TickerSymbol)]
    stockInfo db val = do
      let q = do
          s < - table stock
          restrict (fromNull (constant "") (s!company_name)
                    `like` constant ("%"++val++"%"))
          r <- project (company_name << s!company_name #
                        ticker << s!ticker)
          return r
      rs <- query db q
      return $ map (\\r ->
        (maybe "" id (r!company_name), r!ticker)) rs

To run the query, a database connection detail is passed, along with the
search string. In this case, find all company names and stock tickers
where the company name contains *'news'*.

    :::haskell
    vals :: IO [(CompanyName, TickerSymbol)]
    vals = withDB $ \\db -> stockInfo db "news"

The result is:

    :::haskell
    [("APN NEWS & MEDIA LIMITED","APN"),
     ("WEST AUSTRALIAN NEWSPAPERS HOLDINGS LIMITED","WAN"),
     ("NEWS CORPORATION","NWS"),
     ("NEWSAT LIMITED","NWT")]

The database connection can be abstracted into a separate module:

    :::haskell
    module StockConnection where

    import Database.HaskellDB
    import Database.HaskellDB.HSQL.MySQL

    opts = MySQLOptions {
            server="localhost",
            db="stocks",
            uid="stock_user",
            pwd="stock_pass"}

    withDB :: (Database -> IO a) -> IO a
    withDB = mysqlConnect opts

If you want more information, try:

-   [Introductory Slides][] (pdf) – a gentle introduction.
-   [Student Paper: HaskellDB Improved][] (pdf) – the report of the
    re-write.
-   [Database.HaskellDB.Query][] – list of the query combinators.

This approach to database programming is included in Microsoft's .NET
platform, called [LINQ][]. [Eric Meijer][] is the [link][] between the
two.

  [HaskellDB]: http://haskelldb.sourceforge.net/
  [Introductory Slides]: http://www.cs.chalmers.se/~bringert/publ/haskelldb/haskelldb-db-2005.pdf
  [Student Paper: HaskellDB Improved]: http://haskelldb.sourceforge.net/haskelldb.pdf
  [Database.HaskellDB.Query]: http://hackage.haskell.org/packages/archive/haskelldb/0.10/doc/html/Database-HaskellDB-Query.html
  [LINQ]: http://en.wikipedia.org/wiki/Language_Integrated_Query
  [Eric Meijer]: http://research.microsoft.com/~emeijer/
  [link]: http://research.microsoft.com/~emeijer/Papers/HaskellDB.pdf
