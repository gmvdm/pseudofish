Title: How to install Oracle on Mac OS X 10.4 (Tiger)
Date: 2005-05-26 20:06
Author: gmwils
Category: Apple

Install [instructions][] are now available for getting Oracle to work on
Mac OS X 10.4. I'm happily able to type `sqlplus` in Terminal and not
have link errors. It is even nicer to have my database restored so that
it has something to connect to!

The steps are as follows.

-   Type the command
-   install oracle with oracle installer
-   Type the commands

Now you can run `dbca` and create a database

Note: you must ensure that your `ORACLE_HOME` environment variable is
set before calling the relink all script.

  [instructions]: http://forums.oracle.com/forums/thread.jsp?forum=134&thread=299951&start=45&msRange=15
