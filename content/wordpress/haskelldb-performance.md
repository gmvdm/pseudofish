Title: HaskellDB Performance
Date: 2008-05-18 23:47
Author: gmwils
Category: Haskell

Things did not go well with HaskellDB when I ran my query across a large
data set. MySQL as a query optimizer, sucked. Postgres seems to be doing
better.

I started with a mysql database containing 11 years of day [data][] from
the ASX. This includes the closing price (and some other info) of all
stocks traded on the Australian Stock Exchange (ASX) since 1997.

The tables are organized with unique keys and, based on some testing,
include appropriate indexes.Things still ran slowly.

I tried [tuning mysql][]. Then, based on the slow queries logged, tried
running them by hand to see if I was missing any indexes. No such luck.
The query just didn't perform.

I simplified the query and ran it again (see below). Now it ran fast,
but doesn't help with the generated query. Looks like MySQL's optimizer
doesn't optimize enough.

MySQL timing:

-   Query 1: **6.25s** (anywhere from 24s - 6s)
-   Query 2: 0.15s

Next step. Install Postgres.

Postgres timing:

-   Query 1: 0.03s
-   Query 2: 0.03s

To avoid the cache impacting the results, both servers were stopped and
re-started between each query run. With caching, Postgres gets down to
0.2s. MySQL will still have 6s/0.3s. Tests were run on a MacBook with
2Gb of memory.

Both queries were run with the command line tool of the respective
database engines, mysql and psql. The end\_of\_day table has 4,749,025
records and the stock table has 25,863 records.

Query 1 – HaskellDB generated

    :::sql
    SELECT closing_price2 as closing_price,
           trade_date2 as trade_date
    FROM (SELECT stock_id as stock_id2,
                 trade_date as trade_date2,
                 closing_price as closing_price2
          FROM end_of_day as T1) as T1,
         (SELECT stock_id as stock_id1,
                 ticker as ticker1
          FROM stock as T1) as T2
    WHERE stock_id1 = stock_id2
      AND ticker1 IN ('FXJ','NWS','WAN')
      AND trade_date2 = '2008-02-14 00:00:00';

Query 2 – Hand written

    :::sql
    SELECT e.closing_price as closing_price,
           e.trade_date as trade_date
    FROM
        stock s, end_of_day e
    WHERE
        s.stock_id = e.stock_id
        AND s.ticker IN ('FXJ','NWS','WAN')
        AND e.trade_date = '2008-02-14 00:00:00';

So don't use HaskellDB and MySQL if you are doing joins across large
tables. Use Postgres instead.

The Haskell query:

    :::haskell
    indexStock db tkrs stockDate = do
      let q = do
          s < - table S.stock
          e <- table E.end_of_day
          restrict (s!S.stock_id .==. e!E.stock_id .&&.
                    s!S.ticker `_in` tickers .&&.
                    e!E.trade_date .==. constant stockDate)
          r <- project (closing_price << e!E.closing_price #
                        trade_date << e!E.trade_date)
          return r
          where
            tickers = map (constant) tkrs
    rs <- query db q
    return $ sum $ map (\\r -> read (r!closing_price)) rs

  [data]: http://www.float.com.au/scgi-bin/prod/dl.cgi
  [tuning mysql]: http://www.day32.com/MySQL/
