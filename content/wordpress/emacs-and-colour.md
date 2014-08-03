Title: Emacs and Colour
Date: 2010-10-20 09:53
Author: gmwils
Category: emacs

After spending time with emacs, I really enjoy its support for Clojure.
However, the default colour scheme made me sad.

For vim, I've been using desert and for TextMate, the railscasts colour
theme. Fortunately, someone has already made a Railscast colour theme
for [emacs][]!

Installation was painless. Drop a file into a directory under .emacs.d
and update my .emacs file with:

    :::lisp
    (require 'color-theme)
    (color-theme-initialize)
    (load-file "~/.emacs.d/site-lisp/themes/color-theme-railscasts.el")
    (color-theme-railscasts)

Now emacs loads in a sensible colour scheme and I don't hurt my eyes
while programming.

One more thing I [found][] was the option to set Clojure syntax
highlighting in the repl window:

    :::lisp
    (add-hook 'slime-repl-mode-hook 'clojure-mode-font-lock-setup)

  [emacs]: http://github.com/olegshaldybin/color-theme-railscasts
  [found]: http://github.com/technomancy/swank-clojure
