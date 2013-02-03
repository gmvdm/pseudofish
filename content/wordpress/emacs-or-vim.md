Title: Emacs or Vim
Date: 2011-11-25 01:33
Author: gmwils
Category: Technology

After over 12 years of using Vi(m), and a brief fling with TextMate, I
[started][] [using][] Emacs as my primary editor.

</p>

### Emacs

</p>

The switch has been very positive. The learning curve has been
relatively steep, as my expectations from a text editor are quite high.

</p>

Emacs strength (and weakness) is that it is incredibly extensible. Where
I'm finding Emacs a win over Vim is that I don't have to leave Emacs to
get things done. With Vim, I tend to use more of a mix of terminal
windows and the editor.

</p>

I began by using the [starter kit][] to get going with Emacs
configuration. This made it quicker to get moving, but added a lot of
things I ended up not needing. After getting more comfortable with
elisp, I started from scratch and rebuilt my [emacs.d folder][].

</p>

To jump in quickly, I also purchased the tutorial video from
[Peepcode][]. This certainly helped as emacs is a mental shift coming
from Vim.

</p>

The big benefit I have found with Emacs is the extension packages. These
can be installed from the ELPA [repository][], and include a range of
different *modes*.

</p>

Some of my favourite modes include:

</p>

-   [paredit][] - essential for any lisp, it ensures your brackets
    match.
-   [deft][] - simplified note taking. (I it sync via [Dropbox][])
-   [magit][] - comprehensive Git workflow within Emacs
-   [markdown-mode][] - my current default for writing notes, although
    I'm leaning towards org-mode now.
-   [org-mode][] - highly capable note taking mode, with export options
    to everything. You can use it to write a book, create slides, or
    manage your todo list.

</p>

On the Mac, I've been using [Aquamacs][] for most of my text editing,
and used [macports][] to install the command line client.

</p>

I have yet to try Emacs on Windows, as I haven't been using Windows much
at all. There is a release available [here][].

</p>

After cleaning up my .emacs.d configuration, I've now started using
Emacs on Linux servers I use regularly. For temporary servers, I'll
fallback to Vim as Emacs is often not installed.

</p>

If you want to improve your emacs skills follow @[emacs\_knight][].

</p>

### Vim

</p>

To get started with Vim, it is worth reading [The Vim Learning Curve is
a Myth][].

</p>

<p>
> </p>
>
> Over the years, the popular mythology around vim has become that it’s
> insanely difficult to learn; a task to be attempted by only those with
> the thickest of neck-beards. I’ve heard dozens of times from folks who
> are convinced it will take them months to reach proficiency.
>
> </p>
>
> These beliefs are *false*.

</p>

My feeling is that Vim is unrivalled for the simple task of text
editing. Even after a day or two of learning, you will be faster.

</p>

Where things get a bit more complicated is when you start to realise
that text editing isn't the whole story for a text editor.

</p>

Platform support is superb. The first thing I do to a Windows machine is
install [Vim][]. It is rare for an application with a Unix heritage to
be so comfortable on Windows.

</p>

Historically, I hadn't been a fan of the graphical version of
[MacVim][]. This is something that is much better in recent releases.
Load times are much improved.

</p>

Integration into external tools is where I feel Vim is lacking a bit.
With the number of developers migrating from TextMate to Vim, this gap
is being rapidly addressed. However, Vim isn't as extensible as some
other editors.

</p>

I really noticed this when trying out Clojure programming. If you are
dealing with a REPL based environment, Vim has a way to go.

</p>

### Closing Thoughts

</p>

If you aren't using either of them, it's not too late to start. You
can't make a bad choice.

</p>

If you are already using either Emacs or Vim, enjoy!

</p>

Both are great editors that allow you to be incredibly productive at
working with text. Try learning a new feature each week. You use your
text editor so often that a small improvement is a major payoff.

</p>

  [started]: http://pseudofish.com/blog/2010/09/18/learning-clojure-with-google-app-engine-and-emacs/
  [using]: http://pseudofish.com/blog/2011/04/14/emacs-update/
  [starter kit]: https://github.com/technomancy/emacs-starter-kit
  [emacs.d folder]: https://github.com/gmwils/dotfiles/tree/master/emacs.d
  [Peepcode]: https://peepcode.com/products/meet-emacs
  [repository]: http://www.emacswiki.org/emacs/ELPA
  [paredit]: http://www.emacswiki.org/emacs/ParEdit
  [deft]: http://jblevins.org/projects/deft/
  [Dropbox]: http://emacs-fu.blogspot.com/2011/09/quick-note-taking-with-deft-and-org.html
  [magit]: http://www.emacswiki.org/emacs/Magit
  [markdown-mode]: http://jblevins.org/projects/markdown-mode/
  [org-mode]: http://orgmode.org/
  [Aquamacs]: http://aquamacs.org/
  [macports]: http://www.macports.org/
  [here]: http://www.gnu.org/software/emacs/windows/Getting-Emacs.html#Getting-Emacs
  [emacs\_knight]: https://twitter.com/#!/emacs_knight
  [The Vim Learning Curve is a Myth]: http://robots.thoughtbot.com/post/13164810557/the-vim-learning-curve-is-a-myth
  [Vim]: http://www.vim.org/download.php
  [MacVim]: http://code.google.com/p/macvim/
