Title: Debugging Python with PDB
Date: 2012-05-03 02:51
Author: gmwils
Category: python

I suck at using debuggers, largely because I don't launch them often
enough.

Fortunately, this year's PyCon had a [great talk][] from Chris McDonough
on how to get started with Python's debugger, [PDB][]. The friendly
people at Stockholm's [Python meet-up][] suggested it.

<iframe width="420" height="315" src="http://www.youtube.com/embed/vfPtGsSJldg" frameborder="0" allowfullscreen></iframe>

I made notes while watching, to remove excuses from future me on
launching pdb.

Where you want to have the debugger start, add the following code:

    :::python
    import pdb; pdb.set_trace()

This drops you into a PDB prompt. This is more helpful than putting in
yet more print statements.

Some helpful commands once you're in:

- l - list code
- args - arguments to current function
- p <var\> - print a var
- pp <var\> - pretty print a var
- n - next
- s - step
- w - where (stack trace for current position)
- h - help

While in PDB, you can evaluate python code. The evaluated code won't
impact the running program.

For a bonus trick if you're using Emacs, try out [pdb track mode][].
Launch your python process to be debugged in an emacs shell (M-x shell).
Stepping through the code in pdb will track with a source code buffer.

This worked out of the box with my emacs config. Your milage may vary.

I may actually start to enjoy debugging now!


  [great talk]: http://pyvideo.org/video/644/introduction-to-pdb
  [PDB]: http://docs.python.org/library/pdb.html
  [Python meet-up]: http://www.meetup.com/pysthlm/
  [pdb track mode]: http://wiki.zope.org/klm/PDBTrack
