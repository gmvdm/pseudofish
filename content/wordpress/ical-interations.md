Title: iCal interactions
Date: 2005-08-19 22:14
Author: gmwils
Category: Apple, Python

Apple was nice enough to provide a feature rich interface for the
AddressBook, and so I started my investigations of iCal with high hopes.
Alas, these were to be dashed, and in rather short order.

</p>

XCode documentation wasn't enlightening, Apple's web site was notably
quiet ... something was amiss.

</p>

[This article][] by Rod Schmidt over at O'Reilly started to shine some
light on matters. To quote some key pieces of the puzzle:

</p>

<p>
> </p>
> Apple doesn't provide any APIs to read iCal's data, but you can do it
> yourself.
>
> <p>

</p>

And:

</p>

<p>
> All the data for iCal is stored in .ics files in \~/Library/Calendars.
> There is one .ics file for each calendar you have created.

</p>

Ah ha! A starting point. Now to be honest I don't have much in my iCal
calendars, as I tend to use Exchange for calendaring, so I put a few
things in and then went hunting. To my confusion, no such folder. It had
to be somewhere.

</p>

According to a range of posts, Apple was definitely storing iCal
information in a [standard format][], and with Spotlight now requiring
everything to be files, it had to be somewhere.

</p>

<p>
    % cd ~/Library% find . -name '*.ics'./Application Support/iCal/Sources/711885EF-B88B-44AE-B63E-A1409474922D.calendar/corestorage.ics./Application Support/iCal/Sources/C28120BF-AE28-49AE-8869-E6616428A12A.calendar/corestorage.ics./Caches/com.apple.iCal/inbox.calendar/corestorage.ics

</p>

This didn't look as promising, but at least the .ics files have been
located. Ignoring the cache directory, the other directory names didn't
look particularly nice, but included in each of them is a trusty
Info.plist file that includes some useful properties.

</p>

-   Key - this appears to be the name of the directory and a unique key
    identifying the calendar.
-   Title - Only appears for normal calendars (see below).
-   Type - Two types that I've seen so far are
    `com.apple.ical.sources.naivereadwrite` (normal calendars) and
    `com.apple.ical.sources.birthdays` (birthday calendar).
    </p>
    <p>

</p>

At this point, I think it is safe to assume that the underlying
structures changed somewhat in Tiger (or earlier) from the simplistic
store mentioned in the O'Reilly article. Nothing too tricky though, so
it should be possible to check for either type of directory store and
locate the appropriate files.

</p>

If anyone has further information on iCal file storage, either in terms
of links or corrections to anything I've mentioned, please post to the
comments.

</p>

The next step would be to be able to manipulate these files. If I can
avoid it, I'd rather not write a [RFC2445][standard format] parser.
Fortunately, several people have beaten me to it.

</p>

[iCal.py][] provides a simple interface into the calendar file, with a
simple class that wraps the file. The directory and file loading needs a
bit of messing around with for Tiger.

</p>

I was looking for a bit more and found it in [iCalendar][] by Max M. The
library is LGPL'd which doesn't cause me issues, but may have
implications if you are wanting it for commercial software. Installation
was typical Python style, pain free.

</p>

After installation and changing to one of the directories which contain
my .ics files, the following allowed me to read the calendar (.ics)
file:

</p>

<p>
    >>> from icalendar import *>>> cal = Calendar.from_string(open('corestorage.ics','rb').read())>>> calVCALENDAR({'CALSCALE': 'GREGORIAN', 'VERSION': '2.0', 'PRODID': '-//Apple Computer\\, Inc//iCal 2.0//EN'})>>> for component in cal.walk():...     component.name... 'VCALENDAR''VEVENT'

</p>

The API provides a range of useful documentation and examples, with unit
tests for all the features. These in themselves also provide useful code
snippets for deriving usage. The API also supports creating and
modifying .ics files.

</p>

My aim in all this is to be able to update the underlying data for iCal.
Brief tests show that changing the .ics files while iCal is running
doesn't quite lead to user interface updates. On the bright side, the
Index files seem to be re-generated on closing and opening iCal.

</p>

Further investigation of this should hopefully lead to some way of
coaxing iCal into playing nicely. At the moment I suspect it may involve
a bit of Applescript to drive the application into a refresh if
required.

</p>

(Update: refer to comments for the insight I was missing. On Tiger, Sync
Services does exactly what I'm wanting in terms of keeping a calendar in
sync with my app. For earlier versions, I should be able to live with
exporting a calendar file.)

</p>

  [This article]: http://www.macdevcenter.com/pub/a/mac/2003/09/03/rubycocoa.html
  [standard format]: http://www.ietf.org/rfc/rfc2445.txt
  [iCal.py]: http://www.devoesquared.com/Software/iCal_Module
  [iCalendar]: http://codespeak.net/icalendar/
