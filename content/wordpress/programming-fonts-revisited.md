Title: Programming Fonts Revisited
Date: 2008-05-01 23:09
Author: gmwils
Category: Technology

[Fixed width fonts][] don't play nice with non-Western character sets.

Recently was editing some code in [Vim][] that included strings in
Vietnamese. Ignoring the bit where code and strings shouldn't be in the
same file, the font should at least display properly.

Not good.

Bitstream Vera Sans Mono, my default fixed width font for everything,
did not work.

Playing around a bit, I found Courier New worked perfectly for English
and Vietnamese.

Not wanting to have to swap fonts based on language, I tried out the
other language I use a bit for work, Mandarin Chinese.

Nope.

So I'm now in the unfortunate situation of needing to pick a font for my
programming editor based on the language of the strings mixed in with
the code. Not cool.

My current fonts (on Windows) now look like:

-   Bitstream Vera Sans Mono – English
-   Courier New – English + Vietnamese
-   NSimSun – English + Mandarin

Any suggestions on a good fixed width font with characters for other
languages?

  [Fixed width fonts]: http://pseudofish.com/blog/2007/11/08/programming-fonts/
  [Vim]: http://www.vim.org/
