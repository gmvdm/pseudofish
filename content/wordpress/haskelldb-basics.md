Title: HaskellDB Basics
Date: 2008-05-11 23:35
Author: gmwils
Category: Haskell

[HaskellDB][] is a domain specific embedded language for specifying
database queries and operations.

</p>

The upside of this is the full Haskell language for writing queries and
the Haskell compiler and type checker for validating database code. The
(big) downside is the error messages are horribly cryptic; although once
is compiles it is likely to be correct.

</p>

The original version of HaskellDB was re-written to be more portable and
usable in more situations. Unfortunately, the documentation is out of
step with the current code.

Installation is particularly tricky.

</p>

The following is an example query:

</p>
<p>
    stockInfo :: Database -> String             -> IO [(CompanyName, TickerSymbol)]stockInfo db val = do  let q = do      s < - table stock      restrict (fromNull (constant "") (s!company_name)                `like` constant ("%"++val++"%"))      r <- project (company_name << s!company_name #                    ticker << s!ticker)      return r  rs <- query db q  return $ map (\\r ->     (maybe "" id (r!company_name), r!ticker)) rs

</p>

To run the query, a database connection detail is passed, along with the
search string. In this case, find all company names and stock tickers
where the company name contains *'news'*.

<p>
    vals :: IO [(CompanyName, TickerSymbol)]vals = withDB $ \\db -> stockInfo db "news"

</p>

The result is:

</p>

<p>
    [("APN NEWS & MEDIA LIMITED","APN"), ("WEST AUSTRALIAN NEWSPAPERS HOLDINGS LIMITED","WAN"), ("NEWS CORPORATION","NWS"), ("NEWSAT LIMITED","NWT")]

</p>

The database connection can be abstracted into a separate module:

</p>

<p>
    module StockConnection whereimport Database.HaskellDBimport Database.HaskellDB.HSQL.MySQLopts = MySQLOptions {        server="localhost",         db="stocks",         uid="stock_user",         pwd="stock_pass"}withDB :: (Database -> IO a) -> IO awithDB = mysqlConnect opts

</p>

If you want more information, try:

</p>

-   [Introductory Slides][] (pdf) – a gentle introduction.
-   [Student Paper: HaskellDB Improved][] (pdf) – the report of the
    re-write.
-   [Database.HaskellDB.Query][] – list of the query combinators.

</p>

This approach to database programming is included in Microsoft's .NET
platform, called [LINQ][]. [Eric Meijer][] is the [link][] between the
two.

</p>

  [HaskellDB]: http://haskelldb.sourceforge.net/
  [Introductory Slides]: http://www.cs.chalmers.se/~bringert/publ/haskelldb/haskelldb-db-2005.pdf
  [Student Paper: HaskellDB Improved]: http://haskelldb.sourceforge.net/haskelldb.pdf
  [Database.HaskellDB.Query]: http://hackage.haskell.org/packages/archive/haskelldb/0.10/doc/html/Database-HaskellDB-Query.html
  [LINQ]: http://en.wikipedia.org/wiki/Language_Integrated_Query
  [Eric Meijer]: http://research.microsoft.com/~emeijer/
  [link]: http://research.microsoft.com/~emeijer/Papers/HaskellDB.pdf
