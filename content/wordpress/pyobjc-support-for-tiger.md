Title: PyObjC support for Tiger
Date: 2005-05-04 22:43
Author: gmwils
Category: Musings, Python

[PyObjC adds support for Tiger specific technologies][] - however not in
the current released build. You currently need to grab the source via
subversion.

First, download subversion for Mac OS X from [Martin Ott's site][]. The
10.3 installer seems to work okay for 10.4.

Second, follow the instructions for downloading the PyObjC source:

<p>
    svn co http://svn.red-bean.com/pyobjc/trunk/pyobjc/

</p>

Finally, follow the installation instructions. The short version is:

<p>
    cd pyobjcpython setup.py bdist_mpkg --open

</p>

And then follow the instructions in the installer.

  [PyObjC adds support for Tiger specific technologies]: http://www.pycs.net/bbum/2005/4/29/
  [Martin Ott's site]: http://www.codingmonkeys.de/mbo/
