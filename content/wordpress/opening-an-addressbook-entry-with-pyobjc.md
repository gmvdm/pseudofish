Title: Opening an AddressBook entry with PyObjC
Date: 2005-07-19 21:02
Author: gmwils
Category: Cocoa, Musings, Python

Having done some user testing on my DateList application, I discovered
that they (me and my other test subject) expected something to happen
when double clicking on an entry. It seems reasonable to me to open the
person in Apple's AddressBook as the action.

</p>

There doesn't seem to be much information on this, however playing
around with the birthday calendar (Tiger iCal feature), there is a URL
that seems to work:

</p>

<p>
    addressbook://E15E4D1E-AAE1-4AC2-85DB-98BB906EE988:ABPerson

</p>

Passing this to the `open` shell command opens the appropriate person in
AddressBook.

</p>

The better question is how to construct one of these. To query an
AddressBook entry, we first need to find one. AddressBook has a special
reference for the current user called `me`.

</p>

<p>
    >>> from AddressBook import *>>> book = ABAddressBook.sharedAddressBook()>>> book<ABAddressBook: 0x1133d80>>>> me = book.me()>>> type(me)<objective-c class ABPerson at 0xa4ac3034>

</p>

Now that we have a [ABPerson][], we can determine the UID. The UID
property is actually on the base class, [ABRecord][].

<p>
    >>> myUID = me.valueForProperty_(kABUIDProperty)>>> myUIDu'E15E4D1E-AAE1-4AC2-85DB-98BB906EE988:ABPerson'

</p>

To open a URL, we need to construct a [NSURL][]:

</p>

<p>
    >>> from Foundation import *>>> url = NSURL.URLWithString_('addressbook://' + myUID)>>> urladdressbook://E15E4D1E-AAE1-4AC2-85DB-98BB906EE988:ABPerson

</p>

Finally, we pass the NSURL to the openURL\_ method of the shared
workspace. You get one shared workspace per application, and it can be
used for useful things like opening urls, files, applications and some
other services such as tracking changes.

</p>
<p>
    >>> from AppKit import *>>> ws = NSWorkspace.sharedWorkspace()>>> ws<NSWorkspace: 0x1134910>>>> ws.openURL_(url)1>>> 

</p>

`openURL_` returns YES (1) if the URL was successfully opened, NO (0)
otherwise. At this point AddressBook should open and have selected the
entry that you have tagged as *you*.

</p>

  [ABPerson]: http://developer.apple.com/documentation/UserExperience/Reference/AddressBook/ObjC_classic/Classes/ABPerson.html
  [ABRecord]: http://developer.apple.com/documentation/UserExperience/Reference/AddressBook/ObjC_classic/Classes/ABRecord.html#//apple_ref/occ/cl/ABRecord
  [NSURL]: http://developer.apple.com/documentation/Cocoa/Reference/Foundation/ObjC_classic/Classes/NSURL.html
