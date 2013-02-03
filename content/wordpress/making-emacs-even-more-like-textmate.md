Title: Making Emacs even more like TextMate
Date: 2010-12-23 15:21
Author: gmwils
Category: Ruby, Technology

Much as I love TextMate, I'm still trying to get back to one editor.
Here are a two more things to make Aquamacs even more TextMate like.

</p>

### TextMate Minor Mode

</p>

Go to defunkt's github [page][] and follow the instructions.

</p>

This gives you access to some of the magical TextMate features. The ones
I missed the most are:

</p>

-   ⌘T - Go to File
-   ⌘/ - Comment Line (or Selection/Region)
-   ⌘L - Go to Line

</p>

By adding in these few shortcuts, I find it much easier to jump between
the editors.

</p>

### Cucumber Support

</p>

A simple set of [scripts][] to enable cucumber support into emacs. See
the installation page for how to set it up. And don't forget the
pre-req.

</p>

Once installed, you get syntax highlighting for feature files, and
snippet support.

</p>

You can also setup run targets, however that requires a few [more
dependencies][].

</p>

### Other Rails Files

</p>

Try the [following][] in your .emacs to include additional syntax
highlighting:

</p>

<p>
    ;; Rake files are ruby, too, as are gemspecs, rackup files, etc.(add-to-list 'auto-mode-alist '("\\.rake$" . ruby-mode))(add-to-list 'auto-mode-alist '("\\.gemspec$" . ruby-mode))(add-to-list 'auto-mode-alist '("\\.ru$" . ruby-mode))(add-to-list 'auto-mode-alist '("Rakefile$" . ruby-mode))(add-to-list 'auto-mode-alist '("Gemfile$" . ruby-mode))(add-to-list 'auto-mode-alist '("Capfile$" . ruby-mode))(add-to-list 'auto-mode-alist '("Vagrantfile$" . ruby-mode))

</p>

  [page]: https://github.com/defunkt/textmate.el
  [scripts]: https://github.com/michaelklishin/cucumber.el
  [more dependencies]: https://github.com/michaelklishin/cucumber.el/issues#issue/3
  [following]: https://github.com/technomancy/emacs-starter-kit/raw/master/starter-kit-ruby.el
