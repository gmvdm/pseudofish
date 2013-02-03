Title: Hacking the iTunes library with Python
Date: 2005-07-18 20:23
Author: gmwils
Category: Apple, Musings, Python

[Bob][] was having [a bit of trouble][] with his Airport Express.
Fortunately for the rest of us, his solution involved delving into the
internals of the iTunes library for answers.

</p>

Interesting for the simplicity with which PyObjC allows Python idioms to
mesh with Apple's APIs for a neat solution. With a few lines in an
interactive shell, Bob manages to locate all the problematic files and
set the correct creator code

</p>

  [Bob]: http://bob.pythonmac.org
  [a bit of trouble]: http://bob.pythonmac.org/archives/2005/07/18/airport-express-hates-me/
