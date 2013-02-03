Title: Using TextMate with Google Docs
Date: 2010-06-22 11:19
Author: gmwils
Category: Musings, Technology

The new [Google Command Line][] opens up some interesting possibilities.
One that I wanted to explore was using TextMate to edit basic Google
Docs.

</p>

First, install Google's [Command Line][] tool. Details are on [their
wiki][Command Line] for each OS. There are lots of tips in the comments
and even a [packaged installer][]. (I used `port`s to install)

</p>

The next step is to create a symlink from the "mate" command to
"mate\_wait". What this does is default the wait argument to true. This
is needed for the Google script to detect changes to your document.

</p>

<p>
    sudo ln -s /usr/bin/mate /usr/bin/mate_wait

</p>

You can now open a document in TextMate:

</p>

<p>
    google docs edit --title "Ideas" --editor "mate_wait"

</p>

If you select a title for a document that doesn't exist, it will be
created. Once you close the file in TextMate, control returns to the
shell and the document is updated on Google's servers.

</p>

You are only able to edit in text only mode. So it works best on
documents without any formatting.

</p>

To list your existing documents, try:

</p>

<p>
    google docs list

</p>

  [Google Command Line]: http://google-opensource.blogspot.com/2010/06/introducing-google-command-line-tool.html
  [Command Line]: http://code.google.com/p/googlecl/wiki/SystemRequirements
  [packaged installer]: https://www.dustin.li/Publish/Software/Entries/2010/6/19_GoogleCL_Mac_OS_X_binary.html
