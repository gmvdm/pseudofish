Title: Oracle 10g attacked by the Tiger
Date: 2005-05-06 23:45
Author: gmwils
Category: Apple

[This forum post][] explained through the pain of others how I lost an
evening attempting to install Oracle.

Oracle installation links the various binaries against the specifics of
the local machine. By default, Tiger dev tools enables gcc 4.0, which
breaks the link process with a heap of errors.

Switch to gcc 3.0 using:

    sudo gcc_select 3.3

And it won't show any errors, but still won't work. The issue is that
Oracle 10g depends on some Panther specific libraries.

The only solution at the moment seems to be install on an Mac OS X 10.3
machine and then either upgrade it, or copy the install to a 10.4
machine (and under no circumstances re-link on 10.4).

Until Oracle releases an update of course.

  [This forum post]: http://forums.oracle.com/forums/thread.jsp?forum=134&thread=299951&tstart=0&trange=15
