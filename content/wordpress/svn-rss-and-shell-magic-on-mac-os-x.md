Title: SVN, RSS and shell magic on Mac OS X
Date: 2006-08-19 11:20
Author: gmwils
Category: Apple

Bill Bumgarner has a [wonderful post][] on how to setup an RSS feed for
a SVN server. This is an interesting approach, especially given how most
of my workflow is now RSS based - email, photos, news.

</p>

However, the thing that caught my attention was a little command in the
midst of his shell scripting:

</p>

<p>
    pbpaste > post-commit

</p>

`pbpaste` isn't a command I've come across before, but one that I looked
at and went, "Wow!".

</p>

I'm already a fan of `open` and have attempted to replicate its behavior
on both Windows and KDE to limited success. `pbpaste` is going to make
me miss working on my Mac even more.

</p>

`pbpaste` and its cousin, `pbcopy`, allow you to redirect the clipboard
(PasteBoard) to and from the shell respectively. One of those obvious
integration things that makes life a bit easier.

</p>

Thanks Apple, you've made it harder again to switch away from Mac OS X,
and I don't even have [Time Machine][] ... yet.

</p>

  [wonderful post]: http://www.friday.com/bbum/2006/08/17/howto-adding-an-rss-feed-to-a-subversion-server/
  [Time Machine]: http://www.apple.com/macosx/leopard/timemachine.html
