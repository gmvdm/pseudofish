Title: Mac OS X G5 performance compared to Linux on x86
Date: 2005-06-05 21:46
Author: gmwils
Category: apple

There has been much coverage of the [performance comparison][] posted by
Johan De Gelas at Anandtech.

The aim of the article is supposedly to compare the G5 processor to a
few x86 processors (Xeon & Opteron). However, the chosen operating
systems seem a bit strange. On the x86 hardware, linux was chosen, but
on powerpc hardware, Mac OS X was chosen.

Personally, if I was aiming to benchmark the chip, I would have used
[linux on powerpc][] to remove as many variables as possible from the
comparison.

Given the amount of effort spent tuning apache and mysql for performance
on linux, it doesn't surprise me that it doesn't perform so well on Mac
OS X. I still remember how painful it was to get them to compile on the
early betas, let alone run quickly.

The [theories expressed][] as to why the performance is so bad on Mac OS
X are quite [off the mark][].

Fortunate result of all of this is that Apple may spend some time
investigating how the performance of apache and mysql could be improved.
Although [speculation][] has them heading off for x86 as the answer.
Monday will be interesting.

  [performance comparison]: http://www.anandtech.com/mac/showdoc.aspx?i=2436
  [linux on powerpc]: http://www.debian.org/ports/powerpc/
  [theories expressed]: http://www.anandtech.com/mac/showdoc.aspx?i=2436&p=8
  [off the mark]: http://ridiculousfish.com/blog/?p=17
  [speculation]: http://arstechnica.com/news.ars/post/20050603-4970.html
