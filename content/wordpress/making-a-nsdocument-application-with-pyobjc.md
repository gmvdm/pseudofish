Title: Making a NSDocument application with PyObjC
Date: 2005-06-22 22:02
Author: gmwils
Category: Musings, Python

To break things up a bit, I've been working on a different application,
with the intent to return to the birthday example from Parts [1][],
[2][] and [3][] at a later date.

</p>

I'd been playing with a regular expression builder from the .NET world
and decided that a similar tool for Mac OS X seemed like a good idea. To
be useful, I wanted each regular expression that I was working on to be
treated as a separate document, and to be able to store not only the
regular expression, but also any test data I'd been using.

</p>

Future features will include some form of highlighting, replace
expressions, more ways to run the expression against some data, the
ability to generate code snippets (python, perl, etc) and some graphical
way of building expressions.

</p>

From within XCode, create a new project and select *PyObjC
Document-based Application*. Give the project a name (ie. RegExStudio),
pick somewhere to store it and you should end up with the a working
project that implements a very basic text editor. Build and run the
application to try it out.

</p>

The project wizard creates a bunch of very useful things, however to
make things easier, we are going to use Cocoa Bindings instead of the
connection based version implemented by the wizard. The name of your
project is used in things like the document's type, so where I'm using
RegExStudio, use whatever your application is called.

</p>

To start, open the `RegExStudioDocument.py` file and remove all of the
class implementation, except for the `windowNibName` method. This
defines which NIB file contains the interface for our document.

</p>

You should now have something like:

</p>

<p>
    class RegExStudioDocument(NibClassBuilder.AutoBaseClass):    def windowNibName(self):        return u'RegExStudioDocument'

</p>

The aim is to start with three keys for the controller object to manage:
regularExpression, testString and search. The first two will be standard
strings, with the third a dynamically calculated value based on the
first two. This will allow our result to update as the expression or the
test string change.

</p>

Next up, set some default values. This isn't completely required, but
makes it easier to use. Once I figure out preferences, then these values
will be configurable, but one step at a time.

</p>

<p>
        def init(self):        self = super(RegExStudioDocument, self).init()        self.regularExpression = '\w+'        self.testString = \            'The quick brown fox jumped over the lazy dog.'        return self

</p>

This is all that is required to get the first two keys working, the
third requires another two pieces of code. Firstly, we use python's
regular expression capabilities to do the search. It is also worth
ensuring that an invalid regular expression results in a valid value,
thus the try block:

</p>

<p>
        def search(self):        try:            result = re.search(self.regularExpression,\                 self.testString).group()        except:            return ''        return result

</p>

Secondly, we need to let the object know that this is a calculated
value, and that changes to either of the first two, will update search
key. This is done by setting which keys trigger a change notification,
with the following method:

</p>

<p>
    RegExStudioDocument.\    setKeys_triggerChangeNotificationsForDependentKey_(    [u'regularExpression', u'testString'],    u'search')

</p>

Note that this is a method call on the document itself, not a definition
of a member, so it should be at the same indent level as the class. Put
it at the end of the file for now.

</p>

From within XCode, open the `RegExStudioDocument.nib` file. This will
launch Interface Builder with the user interface for the document.

</p>

Resize the default `NSTextView` so that it takes up a third of the
screen and give it a text label above of *Regular Expression*. Add two
more `NSTextView` controls, with text labels of *Input Text* and *Result
Text*.

</p>

Uncheck *Multiple Fonts Allowed* on all three `NSTextView` controls in
the Inspector window. On the *Result Text* uncheck the *Editable*
option, as attempting to write to the search key will cause errors.

</p>

To use Cocoa bindings, there needs to be a controller object of some
sort. As we are dealing with a single document in each window, drag a
`NSObjectController` object to the Instances pane. Ctrl-drag from the
controller to the `File's Owner` object and connect to the `content`
outlet. This sets the controller up to manage the `RegExStudioDocument`.

</p>

With the controller connected add the three keys, *regularExpression*,
*testString* and *search* to the controller's attributes.

</p>

Bind each of the controls to the appropriate key using the `value`
property. Double click on the `NSTextView` controls to access the right
binding set. A single click will only select the bounding object, which
is a `NSScrollView`.

</p>

Finally, ensure that the *Continuously Updates Values* option is set for
the first two controls. This option will mean that the regular
expression is evaluated on every key press, giving you a live view of
the result.

</p>

![Set Continuously Updates Values][]

Now if you run the application, you can enter in a regular expression
and have it applied to the input text!

</p>

<p>
    % open build/RegExStudio.app

</p>

Before I go, two more pieces of code ... add the following methods to
the RegExStudioDocument class:

</p>

<p>
        def dataRepresentationOfType_(self, aType):        # Create a dictionary to put the variable in        dict = NSMutableDictionary.alloc().init()        dict['regex'] = self.regularExpression        dict['text'] = self.testString        return NSKeyedArchiver.archivedDataWithRootObject_(dict)    def loadDataRepresentation_ofType_(self, data, aType):        # Extract to a NSMutableDictionary        dict = NSKeyedUnarchiver.unarchiveObjectWithData_(data)        self.regularExpression = dict['regex']        self.testString = dict['text']        return True

</p>

The above two methods over-ride existing NSDocument methods and will
encode and decode the regular expression and test data to and from a
[NSKeyedArchiver][]. Behind the scenes, the wizard and the NSDocument
infrastructure have implemented the Save and Open functionality.

</p>

Congratulations, you now have a NSDocument based application which can
save files. The complete example is available [here][].

</p>

*Aside*: In the process of building RegExStudio, I discovered that a
similar tool already [existed][] and also used [PyObjC][]! If you
actually need a tool for regular expressions, RegExplor has a better
feature set ... for now.

</p>

  [1]: http://www.pseudofish.com/blog/2005/05/13/part-1-creating-a-basic-cocoabindings-app-with-pyobjc/
  [2]: http://www.pseudofish.com/blog/2005/05/24/part-2-using-address-book-and-making-an-app/
  [3]: http://www.pseudofish.com/blog/2005/05/29/part-3-using-py2app-to-apple-fy-the-app/
  [Set Continuously Updates Values]: /illustrations/2005-06Updates.jpg
  [NSKeyedArchiver]: http://developer.apple.com/documentation/Cocoa/Reference/Foundation/ObjC_classic/Classes/NSKeyedArchiver.html#//apple_ref/doc/uid/20000837-BCIDHGCF
  [here]: /files/RegExStudio-1.0.zip
  [existed]: http://www.python.net/~gherman/RegexPlor.html
  [PyObjC]: http://pyobjc.sourceforge.net/
