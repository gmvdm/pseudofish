Title: Kill Spam with WordPress
Date: 2005-10-19 19:19
Author: gmwils
Category: Musings

*Update:* Perhaps too much optimism too early. Even with what logically
seems like a good way of stopping comment spam, I'm still receiving
comment spam :(

Back to the drawing board.

As I've mentioned [previously][] the amount of comment spam has been
increasing on my blog. The filtering that [WordPress 1.5][] does is good
enough that no spam had become visible, however the administrative
overhead was starting to become untenable.

Given my math background, I quite liked the [concept][] being used over
on [ridiculous fish][]. The downside to that approach is that for a good
calculation of ∏, you need a lot of comments. Short of letting the spam
through, this blog just doesn't see the level of comments to justify it.
The other downside to the approach is that it needs to be explained to
the user.

Investigating plug-ins for WordPress were always something on my *ToDo*
list, and comment spam is a good enough reason to go looking.

One spam plug-in I found which I liked the idea of is [Bad Behavior][].
The basic premise is that it will attempt to identify a spam bot based
on its behaviour. It will then deny the bot access to the site. The win
for this approach is that it works for more than just comment spam. It
helps out with referrer and other forms of spam, as it returns a 412
error if a bot is detected. There is some hope my stats may become
useful again.

The downside to this approach is that it does use heuristics so isn't
perfect. I haven't spent long testing it on its own, so I can't verify
how good it is or isn't. I'll keep you updated next month if my site
stats return to some level of sanity.

The other plug-in that I installed is called [HashCash][] and shows
promise of being effective against comment spam.

HashCash works by asking the client posting a comment to calculate a
value using JavaScript which is then compared by the server. The author
claims that it has been 100% effective for his site, which seems
reasonable. The number of bots that are going to have client side
JavaScript support seems intuitively to be low.

As more sites improve their spam detection, the spam bots are likely to
get smarter. Fortunately, with WordPress's plug-in architecture, it is a
simple matter of upgrading my spam strategy!

  [previously]: http://www.pseudofish.com/blog/2005/10/04/comment-spam-hits-a-new-level/
  [WordPress 1.5]: http://wordpress.org/
  [concept]: http://ridiculousfish.com/blog/?p=23
  [ridiculous fish]: http://www.ridiculousfish.com/blog/
  [Bad Behavior]: http://www.ioerror.us/software/bad-behavior/
  [HashCash]: http://elliottback.com/wp/archives/2005/05/11/wordpress-hashcash-20/
