Title: PyGame on Mac OS X with PyOpenGL
Date: 2005-12-06 11:22
Author: gmwils
Category: Apple, Musings, Python

As a result of [Richard Jones's talk][] at [OSDC2005][], I decided to
install [PyGame][] to play around with.

The demos in the talk were slick, even to the point where PyGame was
used as the presentation tool. Much more dynamic than PowerPoint.

Unfortunately, install is where a bit of trouble started. There didn't
seem to be a simple explanation as to how to get it functioning on my
Mac. The presentation was great, and on a Mac...

Must be possible!

As with most of these things, the joy is in going down blind alleys,
banging your head against (several) walls and making discoveries. The
only way to truly learn something. Unfortunately, the pain can't be
totally avoided. Without it, there were no mistakes. No mistakes lead to
no need to learn. Or so I kept telling myself.

After several rounds with the wall at the end of the alley, some
libraries I built. Some refused to build. Some I later discovered binary
packages for.

I've included a bunch of links below that point to the required
packages. It should be relatively easy to grab everything and have a
working PyGame installation.

1.  [Python 2.4][]
2.  [PyObjC][]
3.  [Python Numeric][]
4.  [Python Image Library (PIL)][]
5.  [SDL][] - C library for user handling
6.  [SDL\_ttf][] - C library for TrueType fonts
    </p>
    <p>
7.  [SDL\_image][] - C library for image handling
    </p>
    <p>
8.  [SDL\_mixer][] - C library for sound
    </p>
    <p>
9.  [SMPEG][] - C based Mpeg and MP3 library. (*Checkout smpeg from CVS;
    autoconf; automake; ./configure; make; create framework.*)
10. [PyGame][1]
11. [PySDL][] is now in [PyGame][1] - Python binding for SDL

Optional packages:

1.  [PyOpenGL][] - OpenGL bindings for Python
2.  [FreeType][] - TrueType font library, listed as a dependency of
    SDL\_ttf but I have no issues without it (yet?).
    </p>
    <p>

If it helps, my /Library/Frameworks looks like:

    % ls -d [Ss][^t]* Python.frameworkPython.framework/       SDL_mixer.framework/SDL.framework/          SDL_ttf.framework/SDL_image.framework/    smpeg.framework/

Useful things are now available in `/Developer/Python/pygame`, with
`/Developer/Python/pygame/Examples` providing a bunch of examples to
test your installation.

A very big grin spread over my face watching the cube rotate from
typing:

    % python /Developer/Python/pygame/Examples/glcube.py

</p>

  [Richard Jones's talk]: http://osdc2005.cgpublisher.com/proposals/9
  [OSDC2005]: http://osdc2005.cgpublisher.com/timetable.html
  [PyGame]: http://www.pygame.org/install.html
  [Python 2.4]: http://undefined.org/python/
  [PyObjC]: http://pyobjc.sourceforge.net/software/
  [Python Numeric]: http://sourceforge.net/projects/numpy
  [Python Image Library (PIL)]: http://www.pythonware.com/products/pil/
  [SDL]: http://www.libsdl.org/download-1.2.php
  [SDL\_ttf]: http://www.libsdl.org/projects/SDL_ttf/
  [SDL\_image]: http://www.libsdl.org/projects/SDL_image/
  [SDL\_mixer]: http://www.libsdl.org/projects/SDL_mixer/
  [SMPEG]: http://icculus.org/smpeg/
  [1]: http://www.pygame.org/
  [PySDL]: http://sourceforge.net/projects/pysdl/
  [PyOpenGL]: http://pythonmac.org/packages/
  [FreeType]: http://savannah.nongnu.org/download/freetype/
