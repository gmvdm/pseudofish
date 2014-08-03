Title: Safari 3.0 and Taboo
Date: 2007-06-29 13:32
Author: gmwils
Category: apple

In the old days, before 3.0, Safari had an annoying habit. If you
pressed Cmd-Q with many windows and tabs open, then Safari would quit.
This could be incredibly frustrating; especially when you accidentally
pressed Q instead of W.

[Taboo][], a questionable [InputManager hack][], provided a work around.

Safari 3.0 fixes it properly. Apple has included the option of prompting
the user on close if multiple tabs or windows are open.

However, if Taboo is still installed, you cannot close top level
windows.

Taboo lives in one of the following two directories.

    ~/Library/Application Support/SIMBL/Plugins/Library/Application Support/SIMBL/Plugins

Remove it, and Safari 3.0 will work as intended.

  [Taboo]: http://pimpmysafari.com/plugins/taboo-03
  [InputManager hack]: http://culater.net/software/SIMBL/SIMBL.php
