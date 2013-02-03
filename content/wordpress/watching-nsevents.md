Title: Watching NSEvents
Date: 2005-07-27 18:50
Author: gmwils
Category: Cocoa

In the midst of investigating how events are passed around within Cocoa
and I found some interesting information. Based on the [Apple Tech Note
- Mac OS X Debugging Magic][], it is possible to watch all the events as
they are sent.

</p>

I was skeptical, but pleasantly surprised to discover that this still
works if you have a PyObjC app, including one that is sym-linked! (ie.
`python setup.py py2app -A`)

</p>

The magical incantation looks something like:

</p>

<p>
    % defaults write com.mysite.MyApp NSTraceEvents YES% MyApp.app/Contents/MacOS/MyApp

</p>

This will launch the app (MyApp) from the command line, with the events
being sent back to the command line. Opening the application as per
normal will have the events sent to the Console.

</p>

The following will turn of the feature:

</p>

<p>
    % defaults write com.mysite.MyApp NSTraceEvents NO

</p>

The results look something like (line breaks added for clarity):

</p>

<p>
    2005-07-27 18:35:57.599 MyApp [2790]     In Application: NSEvent: type=KeyUp loc=(-395,428) time=152170.8 flags=0x180128 win=0 winNum=15994 ctxt=0xf45f chars='ƒ' unmodchars='f' repeat=0 keyCode=3

</p>

*Note:* the com.mysite.MyApp bit is actually the value of the
CFBundleIdentifier in the Info.plist file. See [here][] for details on
setting this up.

</p>

  [Apple Tech Note - Mac OS X Debugging Magic]: http://developer.apple.com/technotes/tn2004/tn2124.html#SECAPPKITEVENTS
  [here]: http://www.pseudofish.com/blog/2005/05/29/part-3-using-py2app-to-apple-fy-the-app/
