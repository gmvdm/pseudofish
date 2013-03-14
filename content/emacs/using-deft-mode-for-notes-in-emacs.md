Title: Using deft mode for notes in Emacs
Date: 2013-03-14
Author: gmwils

[Deft](http://jblevins.org/projects/deft/) mode is one of my favorite
discoveries of emacs, when combined with the magic of org-mode.

I use the combination of both deft and org-mode almost every day. If I'm doing
an interview, taking notes in a meeting, keeping a personal backlog or ideas
for a project, then this is what I'm using.

Deft solves the problem of where to put text files. Org-mode structures what
goes into them.

Deft can be installed via emacs packaging. I configure it like this:

    :::lisp
    (when (require 'deft nil 'noerror)
      (setq
         deft-extension "org"
         deft-directory "~/Dropbox/Notes/"
         deft-text-mode 'org-mode))


I put the default folder within my Dropbox folder. This ensures notes are
backed up and available on any computer where I'm using Dropbox and emacs.

Once in deft mode (`M-x deft`):

* `RET` -- open the current file
* `C-c C-n / C-RET` -- create a new file (auto named)
* `C-c RET` -- create a new file (prompt for name)
* `C-c C-r` -- rename a file
* `C-c C-d` -- delete a file

To search for a particular file, just start typing and the results are
filtered in the same view.

For me, this has been near perfect for quick note taking. My current notes
folder holds over 150 org files and is still fast to search.

When sharing notes from meetings with others, I use org-mode's export feature
(`C-c C-e A`), then highlight the part I want, and send it to the clipboard (`M-|
pbcopy`) to paste into email.

Getting a solid system for note taking in emacs has helped with how often I
use the same text editor. This was also part of my motivation of migrating my
blog to text files (although markdown formatted).
