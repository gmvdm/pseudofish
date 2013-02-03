Title: Adding Filtering to list by subclassing an NSArrayController
Date: 2005-08-06 14:32
Author: gmwils
Category: Cocoa

In the previous series of articles, we've covered [getting started][],
[basic Address Book][] usage, and [making an app bundle][]. This time,
we'll look at adding in some basic filtering to the list of dates.

</p>

To add filtering, we need to extend the NSArrayController class. The
first step is to create a new python class, `ArrayControllerWithSearch`.
This will extend the standard array controller with a search method.

</p>

<p>
    from PyObjCTools import NibClassBuilderclass ArrayControllerWithSearch(NibClassBuilder.AutoBaseClass):    searchString = None    def search_(self, sender):        self.searchString = sender.stringValue()

</p>

This doesn't do anything particularly interesting, except to store the
search string for the other methods to use. The AutoBaseClass means that
the class we are going to derive from will be specified in Interface
Builder and then allocated dynamically.

</p>

The next step is to over-ride the method that actually lists the objects
in the array, `arrangeObjects_`. (recalling that the underscore is
required for when Objective C wants a ':').

</p>

<p>
    def arrangeObjects_(self, objects):    # retrieve a reference to the same method in the base class    supermethod = super(ArrayControllerWithSearch, \        self).arrangeObjects_            if self.searchString is None or self.searchString == '':        return supermethod(objects)    return supermethod(list(filterObjects(objects, self.searchString)))

</p>

The `supermethod` variable is actually a function pointer to the
arrangeObjects\_ method on the super class. This gets used under either
case, so it is easier to have the code to access this in one place.

</p>

`filterObjects` will be defined next. The search is going to be rather
simplistic in that it will check if the search string is contained
within the name of the person.

</p>

<p>
    def filterObjects(objs, searchString):    lowerSearch = searchString.lower()    for obj in objs:        if(lowerSearch in obj['name'].lower()):            yield obj            continue

</p>

Also, add an import statement for the class in the main application
(main.py):

</p>

<p>
    from PyObjCTools import AppHelperimport DateListDelegateimport ArrayControllerWithSearchAppHelper.runEventLoop(argv=[])

</p>

In Interface Builder, subclass NSArrayController in the Classes tab, and
call the sub class the same name as your custom controller
(ArrayControllerWithSearch). In the Attributes section of the Inspector
(with the Classes tab still selected), add a new Action, called
`search:`

</p>

From the Instances tab, select the NSArrayController for the list of
names. In the Inspector, select Custom Class, and then select the new
controller class:

</p>

![ArrayControllerWithSearch subclass][]

Add a search control to the form. This will call the search\_ method
added to the controller.

</p>

![Search control][]

Now, Ctrl-drag from the search control to the array controller in the
Instances tab. This creates a connection. Select the `search:` action
and then press the Connect button.

</p>

Congratulations! You now have a searchable list of birthdays for all
your friends and family, integrated into your Address Book.

</p>

The complete example is available [here][] and includes a working
application bundle in dist/.

</p>

  [getting started]: http://www.pseudofish.com/blog/2005/05/13/part-1-creating-a-basic-cocoabindings-app-with-pyobjc/
  [basic Address Book]: http://www.pseudofish.com/blog/2005/05/24/part-2-using-address-book-and-making-an-app/
  [making an app bundle]: http://www.pseudofish.com/blog/2005/05/29/part-3-using-py2app-to-apple-fy-the-app/
  [ArrayControllerWithSearch subclass]: /illustrations/2005-08SubClass.jpg
  [Search control]: /illustrations/2005-08Search.jpg
  [here]: /files/DateList-1.4.zip
