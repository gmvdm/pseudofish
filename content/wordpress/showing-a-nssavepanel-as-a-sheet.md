Title: Showing a NSSavePanel as a sheet
Date: 2005-10-16 23:28
Author: gmwils
Category: Cocoa

Using a sheet to display a save panel adds for a significant user
interface improvement. Based on the simplicity of a range of other Cocoa
features, I was surprised at how tricky it was to get working.

The issues had nothing to do with Cocoa per-se, but with the PyObjC
bridge.

Creating the panel and creating the sheet is as follows:

    sp = NSSavePanel.savePanel()       sp.setRequiredFileType_('ics')        sp.setNameFieldLabel_('Export As:')sp.beginSheetForDirectory_file_modalForWindow_modalDelegate_didEndSelector_contextInfo_(\    userDocumentFolder(),'default.ics',\    NSApp().mainWindow(),self,\    'didEndSheet:returnCode:contextInfo:',0)

The tricky bit is the asynchronous callback, which is passed in as an
Objective C selector: `'didEndSheet:returnCode:contextInfo:'`

In Python terms, the following method does the trick:

    def didEndSheet_returnCode_contextInfo_(self, sheet, returnCode, info):    if returnCode == NSCancelButton:        return    # Save the file returned by sheet.filename()    print sheet.filename()

I only had one slight problem. The application crashed when the user
clicked a button on the sheet.

The issue is that the Python bridge has no idea as to the type of the
arguments in the method listed as the callback from the sheet. When the
callback occurs from Cocoa, it goes searching for a method which matches
a specific type signature, as documented in [NSSavePanel][].

An explicit type signature is required for the method to be
discoverable. PyObjC provides a few ways of doing this.

Note: the name of the callback function is up to programmer, which is
why the type signature is important.

The Python 2.4 version (using decorators) looks like:

    from objc import *@objc.signature('v@:@ii')def didEndSheet_returnCode_contextInfo_(self, sheet, returnCode, info):    if returnCode == NSCancelButton:        return    # Save the file returned by sheet.filename()

With the standard version like:

    from objc import *def didEndSheet_returnCode_contextInfo_(self, sheet, returnCode, info):    if returnCode == NSCancelButton:        return    # Save the file returned by sheet.filename()    print sheet.filename()didEndSheet_returnCode_contextInfo_ = objc.selector(\        didEndSheet_returnCode_contextInfo_ , signature='v@:@ii')

With the type information added in, the callback can locate the method
on the object and all is well in the world. Files are saved, memory
protected, everybody is happy.

Almost.

I had a simple question, where did this type string come from?

Searching on Google had resulted in two different strings. Both worked.
However they were quite different.

    @objc.signature('v16@4:8@12i16i20')@objc.signature('v@:@ii')

Somewhere, there had to be an explanation for all of this.

The PyObjC documentation provided some good hints. The [intro][]
mentions the different syntax for specifying the type signature, and
provides an example.

Using a convenience method on AppHelper, the type information does not
need to be explicitly included in the code for the endSheet case:

    from PyObjCTools import AppHelper# Python 2.4@AppHelper.endSheetMethoddef didEndSheet_returnCode_contextInfo_(self, sheet, returnCode, info):   pass# Python 2.3def didEndSheet_returnCode_contextInfo_(self, sheet, returnCode, info):    passdidEndSheet_returnCode_contextInfo_ = AppHelper.endSheetMethod(\        didEndSheet_returnCode_contextInfo_)

This third option provides cleaner code, but still didn't explain where
type signatures come from.

(I must have been a difficult child, a solution isn't enough, the need
to know why/how is the motivator)

The key came in reading through the documentation on [wrapping][] an
Objective C class. When the documentation refers to a 'raw Objective-C
method signature', it means what it says. The string appears to be
Objective-C's internal representation of the type signature.

Apple provides [documentation][] on the syntax. (Note: Try [here][] for
updated docs)

Probably a bit further into Objective-C than I wanted to delve, but much
was learnt along the way. A good abstraction allows you to peek through
it. I'm happy to learn that PyObjC provides that flexibility, and that
most of the time, it isn't needed.

</p>

  [NSSavePanel]: http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/ObjC_classic/Classes/NSSavePanel.html
  [intro]: http://pyobjc.sourceforge.net/doc/intro.php#messages-and-functions
  [wrapping]: http://pyobjc.sourceforge.net/doc/wrapping.php
  [documentation]: http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/index.html?http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/RuntimeOverview/chapter_5_section_6.html#//apple_ref/doc/uid/20001425-TPXREF165
  [here]: http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/Articles/chapter_13_section_9.html#//apple_ref/doc/uid/TP30001163-CH9-TPXREF165
