Title: Saving a file using NSSavePanel
Date: 2005-10-01 21:17
Author: gmwils
Category: Cocoa, Python

Saving a file was something I'd been avoiding for a while, as I hadn't
been able to find the right control in Interface Builder to make it
happen. This had led me to believe it was going to be difficult and was
delayed for a long time.

</p>

Today, I bit the bullet and spent some time to figure this out. My
suspicion was that there existed a control that would do the work for
me, as file handling is quite consistent from a UI perspective in Mac OS
X. Reading through [Cocoa Programming][] didn't provide any
enlightenment, so I went back to the XCode documentation.

</p>

By this stage of my Cocoa learning, I really should have known better.
Apple's documentation has solved too many problems for me to be
consulting it as a last resort. Unfortunately, I suspect it is a lesson
I will have to keep learning.

</p>

Apple provides [this information][] about the [NSSavePanel class][].
Finding this class was my 'aha!' moment for the day. No wonder I
couldn't find it in Interface Builder, it isn't an IB control in the
normal sense.

</p>

In Python, the simple version looks something like:

</p>

<p>
    from AppKit import *def saveFile_(self):    sp = NSSavePanel.savePanel()    sp.setRequiredFileType_('ics')    if sp.runModal() < = 0:        return    print 'Filename: ' + sp.filename()

</p>

This will throw a standard file save modal dialog box and ask for a
filename to save. There are a bunch more options on the NSSavePanel
class, which I may explore later. The interesting part will be making
the save panel appear in a [sheet][].

</p>

Something to explore later.

</p>

  [Cocoa Programming]: http://www.amazon.com/exec/obidos/ASIN/0672322307/pseudofish-20?creative=327641&camp=14573&link_code=as1
  [this information]: http://developer.apple.com/documentation/Cocoa/Conceptual/AppFileMgmt/index.html#//apple_ref/doc/uid/10000056i
  [NSSavePanel class]: http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/ObjC_classic/Classes/NSSavePanel.html
  [sheet]: http://developer.apple.com/documentation/Cocoa/Conceptual/Sheets/index.html#//apple_ref/doc/uid/10000002i
