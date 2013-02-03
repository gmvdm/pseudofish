Title: Application behaviour on last window close
Date: 2005-12-01 22:07
Author: gmwils
Category: Cocoa

I grew up with Microsoft's various windowing systems, and learnt the X
Windows style of things while at Uni. When I first used a Mac, Apple's
approach of keeping the application alive after its windows are closed
felt strange.

</p>

Now, having used OS X from early beta stages, I'm more comfortable with
the approach and consider it the norm. Unfortunately, Apple is somewhat
inconsistent with the behaviour.

</p>

It is seemingly on an application by application basis whether or not
the application will quit when the main window is closed. System
Preferences used to persist but now closes. iTunes stays open, iSync
closes and AddressBook stays open!

</p>

For my own application, the decision on this has consumed much of my
time. The code to make the application quit on window code is quite
simple. Add the following two lines to the application delegate:

</p>

<p>
    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):    return True

</p>

The Apple app that is closest to my own is AddressBook, so when in doubt
I have emulated the AB behaviour. Partially for the benefit of users and
partly for my own sanity.

</p>

As I start designing new applications, I end up with the same problem of
which behaviour to choose. My default is to persist the application
unless I get a large number of user complaints. To choose otherwise? I
may as well write Windows programs.

</p>

