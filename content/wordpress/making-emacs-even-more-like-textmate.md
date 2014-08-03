Title: Making Emacs even more like TextMate
Date: 2010-12-23 15:21
Author: gmwils
Category: emacs

Much as I love TextMate, I'm still trying to get back to one editor.
Here are a two more things to make Aquamacs even more TextMate like.

### TextMate Minor Mode

Go to defunkt's github [page][] and follow the instructions.

This gives you access to some of the magical TextMate features. The ones
I missed the most are:

-   ⌘T - Go to File
-   ⌘/ - Comment Line (or Selection/Region)
-   ⌘L - Go to Line

By adding in these few shortcuts, I find it much easier to jump between
the editors.

### Cucumber Support

A simple set of [scripts][] to enable cucumber support into emacs. See
the installation page for how to set it up. And don't forget the
pre-req.

Once installed, you get syntax highlighting for feature files, and
snippet support.

You can also setup run targets, however that requires a few [more
dependencies][].

### Other Rails Files

Try the [following][] in your .emacs to include additional syntax
highlighting:

    :::lisp
    ;; Rake files are ruby, too, as are gemspecs, rackup files, etc.
    (add-to-list 'auto-mode-alist '("\\.rake$" . ruby-mode))
    (add-to-list 'auto-mode-alist '("\\.gemspec$" . ruby-mode))
    (add-to-list 'auto-mode-alist '("\\.ru$" . ruby-mode))
    (add-to-list 'auto-mode-alist '("Rakefile$" . ruby-mode))
    (add-to-list 'auto-mode-alist '("Gemfile$" . ruby-mode))
    (add-to-list 'auto-mode-alist '("Capfile$" . ruby-mode))
    (add-to-list 'auto-mode-alist '("Vagrantfile$" . ruby-mode))

  [page]: https://github.com/defunkt/textmate.el
  [scripts]: https://github.com/michaelklishin/cucumber.el
  [more dependencies]: https://github.com/michaelklishin/cucumber.el/issues#issue/3
  [following]: https://github.com/technomancy/emacs-starter-kit/raw/master/starter-kit-ruby.el
