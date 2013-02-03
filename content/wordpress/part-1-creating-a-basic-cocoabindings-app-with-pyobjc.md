Title: Part 1 - Creating a basic CocoaBindings app with PyObjC
Date: 2005-05-13 22:18
Author: gmwils
Category: Cocoa, Musings, Python

Python provides a clean, easy to learn, easy to develop in programming
language. Cocoa provides a rich, easy to program framework for building
applications on Mac OS X. Given that development should be easy, add
PyObjC into the mix and the richness of Cocoa is available naturally
from within Python. Now to see how easy it is to write a very simple
application.

</p>

My first steps with attempting to create a Cocoa application with Python
involved working through the [tutorial][] on the [PyObjC site][]. This
is a very good place to start if you have an understanding of Cocoa.
Some understanding of [Python][] will also be helpful.

</p>

*Note:* If you are running on Tiger, you'll need the latest [version][].

</p>

The most important thing to learn is how to build one of the sample
applications:

</p>

<p>
    python setup.py py2app -A

</p>

This will create an application bundle to run in the `dist` directory,
using symbolic links to the code. As your source code is linked rather
than copied, any changes you make are reflected in the bundle so you
don't need to re-deploy. Just re-run the application and you will be
using the new code.

</p>

It is worth spending some time playing with some of the samples. The
PyObjC team have done a **very** good job of putting together a wide
range of examples. See `/Developer/Python/PyObjC/Examples` on your
system. Try changing the files around a bit, I find it a useful way to
learn when I break things by trying to add new stuff.

</p>

The first step in making your own application is to create a build
script. This contains the information that `py2app` will use to generate
your Cocoa application. A basic version looks like:

</p>

<p>
    from distutils.core import setupimport py2appsetup(    app=['main.py'],    data_files=['English.lproj'])

</p>

The `app` field is the name of the python file that will be called
first. In some of the examples this is called `__main__.py` and in
others it is the name of the application. I don't like underscores so
much, so I'm going with `main.py`.

</p>

The `data_files` field contains a list of directories in which data
files are stored. For the moment, the only data file that you need to
consider is the NIB files. These specify the interface for your
application and are created by Interface Builder. If you wanted to load
images and various other data, your entry might look like:

</p>

<p>
    data_files=['English.lproj', 'data', 'images']

</p>

The next step is to create the main file, in this case, `main.py`:

</p>

<p>
    from PyObjCTools import AppHelperimport DateListDelegateAppHelper.runEventLoop(argv=[])

</p>

The first line imports the `AppHelper` which is then called to run the
main event loop for the application. This does a range of interesting
Objective C / Cocoa interactions behind the scene, but thanks to PyObjC,
we don't need to worry about that.

</p>

The second line imports the python file that we will now create,
`DateListDelegate.py`.

</p>

<p>
    from PyObjCTools import NibClassBuilderNibClassBuilder.extractClasses('MainMenu')class DateListDelegate(NibClassBuilder.AutoBaseClass):    def items(self):        return []

</p>

There are two important things that happen in this script. Firstly, our
user interface is loaded using the `NibClassBuilder`. Secondly, we
create a class to use in our interface which is going to provide us with
a list of data. For the moment, we simply return the empty list `[]`.

</p>

I'm not going to explain in detail how to use [Interface Builder][].
What I am going to do is to work through what is required to make our
simple application fly.

</p>

From Interface Builder, create a new Cocoa Application and store it as
`MainMenu` in a sub-folder called `English.lproj`. You may need to
create this folder if you haven't previously.

</p>

Next, add an NSTableView to your Window. This control is available in
the Cocoa-Data palette. The palette(s) are the bunch of controls that
should turn up in the top-right of your screen.

</p>

![Cocoa Data palette][]

If you select Test Interface from the File menu in Interface Builder,
you should see your window with a completely empty box. Not particularly
compelling yet, but one step at a time.

</p>

You can now run your application from the command line. Save the Nib and
build a linked version. It is easier to use linked for now as we will be
changing the python files a bit and it saves re-deploying each time you
run the application.

</p>

<p>
    % python setup.py py2app -A% open dist/main.app

</p>

We now need to let Interface Builder know how to talk to the Python
class we created earlier in `DateListDelegate.py`. In the MainMenu
window, jump to the Classes tab and scroll left lots until you see the
`NSObject` class. With that selected, from the Classes menu chose
Subclass NSObject, and name your new class: `DateListDelegate`.

</p>

It is important that this class name exactly matches the class name that
you create in Python, as some Cocoa magic happens behind the scenes to
glue this all together.

</p>

With your new class highlighted, choose the Instantiate DateListDelegate
option from the Classes menu. You should now have a funky blue cube in
the Instances tab of the MainMenu window.

</p>

We need to have our class managed for us, so we'll connect it to the
application. To do this hold down Control then click and drag from the
File's Owner instance to the DateListDelegate instance. You should see
the Outlets tab of the Connections view of the Inspector. From the
Inspector, select the Connect button. This will connect our delegate
class with the delegate property of the main application.

</p>

In order to join together the control on the Window with our Delegate
class, we need a Controller object. This is where CocoaBindings really
help us out, as you just need to drag a NSArrayController from the
Cocoa-Controllers palette to the Instances tab of the MainMenu window.

</p>

![Building blocks][]

Now we get up to the fun part, gluing it all together!

</p>

Firstly, we need some test data to play with. In a future article, I'm
going to look at populating this from an external source, but for now we
are just looking at the user interface, so we can fake it.

</p>

Open up the `DateListDelegate.py` file and update the `items` method to
look something like:

</p>

<p>
    def items(self):    return [        {'date': 1980, 'name': 'John Doe'},        {'date': 1970, 'name': 'Amanda Smith'},        {'date': 1960, 'name': 'Bill Branson'}    ]

</p>

The data representation is how the Key-Value pairs, used by
CocoaBindings, are constructed in Python. This is something that will be
covered in more detail when we look at generating the structure from
real data. If you want more information, see the [Key-Value Coding][]
section of the Apple developer site, or look through the examples in
PyObjC.

</p>

The keys in our example are `date` and `name`, so we'd better let our
Controller know that these are the fields it is going to be looking
after.

</p>

In the Attributes section of the Inspector (Tools-\>Show Inspector) with
the NSArrayController selected, there is an Add button. Add two keys,
and rename them to the names that we have assigned in the data we are
providing, `date` and `name`.

</p>

Not much use, unless our controller knows how to access our data. This
is achieved from the Bindings view of the NSArrayController in the
Inspector.

</p>

Drop down the contentArray property, and select "File's Owner
(NSApplication)" as the Bind to: value.

</p>

Then enter the following into the Model Key Path:

</p>

<p>
    delegate.items

</p>

You should now see the following in the Inspector:

</p>

![Binding the delegate][]

</p>

If you try running the application now, you'll notice we are not quite
there yet. Our controller knows about the data, our table knows about
the array that populates it, but the columns don't know what to show.

</p>

Double click on the title area of the first column in the NSTableView
that is on the Window. This selects the actual table column, and also
allows you to enter in a heading. Call the first one Name.

</p>

Then in the Bindings view in the Inspector, drop down the value property
and select `name` from the Model Key Path: combo box. You should notice
that our key names are pre-populated in this combo box, thanks to the
binding to the controller.

</p>

Repeat the process for the second column, binding that to the date key.

</p>

Our application can now be tested, simply by running it from the command
line:

</p>

<p>
    % open dist/main.app

</p>

Try clicking on a column title and your list should automatically sort,
both by name and by date. All without writing any sorting code, or any
event code for the click to select columns.

</p>

![Completed application][]

To build a distributable version of the application, re-build without
the symbolic link option:

</p>

<p>
    % python setup.py py2app% open dist/main.app

</p>

This will create an application bundle that can be deployed to a Mac OS
X machine that doesn't include PyObjC. This means that your user has no
way of knowing that you've built a Cocoa app without writing a line of
Objective C code.

</p>

Where to from here? It is worth looking through the examples included
with PyObjC as they cover a wide variety of programming topics in Cocoa.
In the next article, we'll look at adding some actual features so it
deserves to be called an application.

</p>

The source code for the sample application from this tutorial is
available [here][].

</p>

<u>Additional articles</u>

</p>

[Part 2 - Integrating Address Book][]

</p>

[Part 3 - Making it look like an application][]

</p>

<u>Bonus link</u>

</p>

[Birthday Notes - finished, open source app, based on these articles][]

</p>

  [tutorial]: http://pyobjc.sourceforge.net/doc/tutorial.php
  [PyObjC site]: http://pyobjc.sourceforge.net/
  [Python]: http://www.pseudofish.com/blog/2005/05/11/learning-python/
  [version]: http://www.pseudofish.com/blog/2005/05/04/pyobjc-support-for-tiger/
  [Interface Builder]: http://developer.apple.com/tools/interfacebuilder.html
  [Cocoa Data palette]: /illustrations/2005-05Cocoa-Data.jpg
  [Building blocks]: /illustrations/2005-05MainMenu.jpg
  [Key-Value Coding]: http://developer.apple.com/documentation/Cocoa/Conceptual/KeyValueCoding/index.html?http://developer.apple.com/documentation/Cocoa/Conceptual/KeyValueCoding/Concepts/Validation.html
  [Binding the delegate]: /illustrations/2005-05Delegate.jpg
  [Completed application]: /illustrations/2005-05Window.jpg
  [here]: http://www.pseudofish.com/files/DateList-1.0.zip
  [Part 2 - Integrating Address Book]: http://www.pseudofish.com/blog/2005/05/24/part-2-using-address-book-and-making-an-app/
  [Part 3 - Making it look like an application]: http://www.pseudofish.com/blog/2005/05/29/part-3-using-py2app-to-apple-fy-the-app/
  [Birthday Notes - finished, open source app, based on these articles]:
    http://www.pseudofish.com/blog/2005/12/23/birthday-notes/
