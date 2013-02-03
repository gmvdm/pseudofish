Title: Re-opening the main NSWindow
Date: 2005-09-21 21:21
Author: gmwils
Category: Cocoa, Musings, Python

I was faced with what seemed a very simple problem, when I closed the
window on my application, I didn't have a way to open it again. For a
document based application, it isn't too much of an issue, the framework
allows you to open or create a new document.

Mac OS X is a bit divided at the moment on this functionality. There are
some single window apps that behave this way, and others that close
themselves when you close the main window. System Preferences is an
example of this.

For my application, I wanted it to have a single main window, and I
wanted the user to be able to click on the dock icon and have it re-open
if it wasn't already there. Same as Mail, Address Book, iTunes and
others.

The trick to making this happen is the
applicationShouldHandleReopen:hasVisibleWindows: method of your
application delegate. This method is called with the NSApplication and a
flag to indicate whether or not any windows are visible for the
application.

    :::python
    def applicationShouldHandleReopen_hasVisibleWindows_(self, theApp, hasVisibleWindows):
        if hasVisibleWindows:
            return True
        for win in theApp.windows():
            # Autosave Name set in .nib
            if win.frameAutosaveName() == 'mainWindow':
                win.makeKeyAndOrderFront_(NSNormalWindowLevel)
                return False

        return True

To be honest, my first version was a bit simpler again, the for loop
looked remarkably like:

    :::python
    win = theApp.windows()[0]

Too many years programming and I couldn't leave the `[0]` alone. Given
that there could be more than one window in my application, I needed a
way to identify the window that I needed to open. Cocoa provides such a
feature, the AutoSave name for a window. This property can be set in
Interface Builder.

Simply give your main window a name, I chose 'mainWindow', and search
for a window with that name.

Once you have a handle on the NSWindow, you need to call
`makeKeyAndOrderFront:`. This method makes the window the *Key* window,
which gives it keyboard focus and makes it visible. The method requires
a window level and given that the main window isn't doing anything
strange, I used NSNormalWindowLevel.

The test for visible windows is a bit of a shortcut. If there is already
a visible window, I don't want any extra ones showing up, so I return
True and let Cocoa deal with the Dock click (or Application open) as it
normally would. If I did open a window, then I return False, as there is
nothing further for Cocoa to do.

In the end, a simple solution to a simple problem.

