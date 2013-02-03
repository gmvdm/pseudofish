Title: Binding to a NSTextView
Date: 2005-06-15 22:00
Author: gmwils
Category: Musings

If you have done much Cocoa programming previously, you may find this
amusingly obvious. However if you are learning from the start, this may
trip you up. So I'll share my lesson that I learnt today.

I'm working on a very simple single object binding exercise. I wanted to
have properties of the object displayed in different NSTextView
controls. However, when I clicked on one, the only binding options I had
were `hidden` and `tooltip`.

Not particularly useful, so I swapped to NSTextField controls only to
find that they didn't support multiple lines. After spending some time
[RTFM][]'ing, I found that there is a bit more to the NSTextView than
was initially apparent to me. It actually has a whole wealth of things
to bind to. The caveat is that in Interface Builder, you need to double
click on the control in order to select the text area within.

The [NSTextView][] reference also mentions that different bindings are
available depending on what options you enable on the control. By
selecting single font (which makes sense for my app), there appears a
binding control for `value` which takes a simple string, just like
NSTextField.

For future reference, if the class name in the heading of the Inspector
window isn't the one you thought it should be or the control's class
ends in *View*, then try double clicking the control. This works for
columns in NSTableView, the text in a NSTextView and the columns in a
NSOutlineView.

  [RTFM]: http://en.wikipedia.org/wiki/RTFM
  [NSTextView]: http://developer.apple.com/documentation/Cocoa/Reference/CocoaBindingsRef/BindingsText/NSTextView.html
