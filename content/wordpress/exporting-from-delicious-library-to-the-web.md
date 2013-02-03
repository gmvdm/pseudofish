Title: Exporting Delicious Library to the web
Date: 2005-10-07 23:06
Author: gmwils
Category: Apple, Python

I've been using [Delicious Library][] for a while now and have been
incredibly happy with the results. I even managed to figure out which
books I had on loan and more importantly discovered I was missing some
books from my collection!

The other thing I'd been playing with was including some books on this
site that I like. You may have noticed them down the side. There is a
bit of PHP code behind the pictures, but I still need to add in the
Amazon id number for each book.

My aim is to use Delicious Library to keep track of my physical media,
including rating it, and to publish the highest rated media onto the
site. Given that Library is basically a thick client built on top of
Amazon, I could even include my referrer link, so if anyone buys
anything I get a small commission to feed my book buying habits.

Library supports exporting its catalog as a tab separated file. I had
hoped for an 'Export to XML' option, so it would be simple XSL transform
and tada!

Given the Python focus of this site, it didn't take long before I had a
workable script up and running.

The important bits of the script are included below:

    :::python
    from Kid import *
    import sys

    def normalizeString(str):
        return str.replace('//', '/').replace('/ ',
        '<br/>').replace('*','<br/>*')

    file = open(sys.argv[1], 'rb')
    for line in file:
        lines.append(line[:-1])
        headings = lines[0].split('\t')
        books = [dict(zip(headings, normalizeString(line).split('\t'))) for line in lines[1:]]

    Template(file='template.kid', books=books).serialize()

The `Template` object is from the [Kid template library][], which is
responsible for generating the resultant XHTML. The *template.kid* file
that I used iterates through the list of dictionaries of books and
displays as links the ones that I've given a rating of (5/5).

    :::html
    <?xml version='1.0' encoding='utf-8'?>
    <html xmlns='http://www.w3.org/1999/xhtml' xmlns:py='http://purl.org/kid/ns#'>
    <head><title>Delicious Library</title></head>
    <body>
      <ul>
        <li py:for='book in books' py:if="book['rating'] == '5'">
          <a py:attrs="href='http://www.amazon.com/exec/obidos/ASIN/' +
            book['asin'] +
            '/pseudofish-20?creative=327641&camp=14573&link_code=as1'">
              ${book['title']}
          </a>
        </li>
      </ul>
    </body></html>

The end result, is that I can now add books into Library as I purchase
and read them, and if I rate the book highly enough then it will turn up
[on this blog][].

Source code and samples are available [here][]. Requires [Delicious
Library][] (full or demo) and [Kid][Kid template library].

  [Delicious Library]: http://www.delicious-monster.com/
  [Kid template library]: http://kid.lesscode.org/
  [on this blog]: /blog/books/
  [here]: /files/DelLib.zip
