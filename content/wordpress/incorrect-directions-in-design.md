Title: Incorrect directions in design
Date: 2005-06-08 21:38
Author: gmwils
Category: Musings

For the amusement of others I'm going to share with you what will
hopefully provide an instructive story in my misadventures in software
design. We are in the midst of a crusade at my day job for updating the
installers for our products. Given that we make Windows software,
installers are key, and a good one adds to the user experience.

</p>

After witnessing the beauty of how installers can magically be made as
part of the build process, after building PyObjC, I set out on a
mission. My goal: create a wonderful installer for my sample
application.

</p>

(as an aside, if you are building Windows you need to check out [WiX][].
Microsoft made this, use [this][] and then [open sourced this][]. Very
cool.)

</p>

Many hours later, after reading all of the documentation for
[bdist\_mpkg][], reading through a whole bunch of source code, using
grep over a whole bunch more and reading yet more stuff, I finally gave
up. In caving, I packaged together the closest that I'd managed to get
into an email.

</p>

[Some one much wiser][] than me provided with very enlightening insight:

</p>

<p>
> </p>
> Don't create installers for applications.
>
> <p>

</p>

Simple really.

</p>

The blinding obviousness of this truth took some time to sink in. When
on a mission, it takes a while for me to re-group. I consulted my
memory. Yep. Every product on my mac that *needed* an installer I
disliked. The applications I [like][], simply provided me with the
application bundle and I could put it anywhere I wanted!

</p>

I was so convinced that I needed an installer, that I'd neglected to
take a step back and look at my assumptions. On the bright side, I now
know much more about the [distribution][] of python modules than ever
before.

</p>

Lesson for others, for Mac OS X, don't create installers for
applications, but if you need to install a python module, the [hard
work][bdist\_mpkg] has been done for you

</p>

  [WiX]: http://www.tramontana.co.hu/wix/index.html#TOC
  [this]: http://blogs.msdn.com/robmen/archive/2004/04/05/107709.aspx
  [open sourced this]: http://sourceforge.net/projects/wix/
  [bdist\_mpkg]: http://undefined.org/python/py2app.html
  [Some one much wiser]: http://bob.pythonmac.org/
  [like]: http://www.adiumx.com/
  [distribution]: http://docs.python.org/dist/dist.html
