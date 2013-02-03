Title: Calendar Sync
Date: 2008-03-06 15:36
Author: gmwils
Category: Musings, Technology

I'm convinced that sync is a big thing. There are lots more players in
this space, attempting to solve a simple problem: We use many devices.

My [calendar][] has lived in Outlook/Exchange for many years, and our
corporate IT policies has made it hard to re-use this data. Google and
Apple, combined, made my day.

1.  [Google Calendar Sync][] - sync between Google Calendar and Outlook
2.  [iCal][] - subscribe to remote calendars
3.  [iSync][] - sync my calendar to my phone and .Mac

The final result is that I can manage my calendar on my PC, and view it
on the web, share it with others, see it on my various Apple computers
and have it updated into my phone.

The astute reader will notice that I can't update my Outlook calendar
with this setup. And that's the way I set it, so I don't risk corruption
of Outlook.

When multiple services are sync'd together, like my calendar example,
you start to have sync messages flying all over the place. Add in some
other common data points, like contacts, email, bookmarks, etc, and it
starts to get messy.

At an enterprise level, this was "solved" using an [ESB][]. The solution
in consumer space is for one sync broker to be the master. And this has
led to a race to be the master sync point. Google, Apple, and [Plaxo][]
are all contenders.

Sync gives you the best of both worlds, access to your information in
the cloud, while keeping it up-to-date on your desktop and in your
pocket.

Competition in this space is a win for all of us.

  [calendar]: http://www.google.com/calendar/embed?src=gmwils%40gmail.com&ctz=Australia/Brisbane
  [Google Calendar Sync]: http://www.google.com/support/calendar/bin/answer.py?answer=89955
  [iCal]: http://en.wikipedia.org/wiki/ICal
  [iSync]: http://en.wikipedia.org/wiki/ISync
  [ESB]: http://en.wikipedia.org/wiki/Enterprise_service_bus
  [Plaxo]: http://en.wikipedia.org/wiki/Plaxo
