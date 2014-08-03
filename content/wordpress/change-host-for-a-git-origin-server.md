Title: Change Host for a Git Origin Server
Date: 2010-06-28 21:19
Author: gmwils
Category: technology

Hopefully this isn't something you need to do. The server that I've been
using to collaborate on a few git projects with had the domain name
expire. This meant finding a way of migrating the local repositories to
get back in sync.

**Update:** Thanks to @[mawolf][] for pointing out there is an easy way
with recent git versions (post Feb, 2010):

    git remote set-url origin ssh://newhost.com/usr/local/gitroot/myproject.git

See the [man page][] for details.

If you're on an older version, then try this:

As a caveat, this works only as it is the same server, just with
different names.

Assuming that the new hostname is "newhost.com", and the old one was
"oldhost.com", the change is quite simple.

Edit the .git/config file in your working directory. You should see
something like:

    [remote "origin"]
    fetch = +refs/heads/*:refs/remotes/origin/*
    url = ssh://oldhost.com/usr/local/gitroot/myproject.git

Change `oldhost.com` to `newhost.com`, save the file and you're done.

From my limited testing (git pull origin; git push origin; gitx)
everything seems in order. And yes, I know it is bad form to mess with
git internals.

  [mawolf]: http://twitter.com/mawolf/status/17334075193
  [man page]: http://www.kernel.org/pub/software/scm/git/docs/git-remote.html
