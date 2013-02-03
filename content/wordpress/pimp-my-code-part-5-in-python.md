Title: Pimp My Code, Part 5: In Python
Date: 2005-10-03 22:17
Author: gmwils
Category: Cocoa, Musings, Python

Wil Shipley continues his *Pimp My Code series* with an [article][]
reviewing what should have been a very simple method to return a path
inside the Application Support folder.

</p>

Well worth a read, both for the stylistic as well as the comedic
commentary.

</p>

From my perspective, it is also a useful source of learning about Cocoa
from one of the better programmers.

</p>

In Python, the final example looks something like:

</p>

<p>
    from Foundation import *def applicationSupportFolder():    return NSSearchPathForDirectoriesInDomains(\        NSApplicationSupportDirectory, NSUserDomainMask, True\    )[0].stringByAppendingPathComponent_(\        NSProcessInfo.processInfo().processName())

</p>

Note: The code has been reformatted to (attempt to) fit your screen.

</p>

  [article]: http://wilshipley.com/blog/2005/10/pimp-my-code-part-5-special-apple.html
