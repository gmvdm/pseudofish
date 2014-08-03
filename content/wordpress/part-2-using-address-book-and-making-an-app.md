Title: Part 2 - Using Address Book and making an app
Date: 2005-05-24 22:04
Author: gmwils
Category: python

Having successfully created a simple Cocoa application using Python in
[Part 1][], the next step is to integrate data from Apple's Address Book
(AB).

The [PyObjC][] example of Address Book usage is a good place to start,
and the [Apple documentation][] includes any other information needed. I
started with the example, played around a bit and then read the
documentation mainly for the constants to get the fields I wanted.

The first step is to create a separate file to include the Address Book
interaction. I put this into `DateList.py`. For a simple start, I've
made the interaction a function that returns the data to the Delegate
class. This is called `dateFields()`, and it creates a connection to the
Address Book and loads the fields for it.

    :::python
    import AddressBook

    def dateFields():
      book = AddressBook.ABAddressBook.sharedAddressBook()
      return bookFields(book)

`bookFields` generates the actual list using a list comprehension.
`validPerson` filters the list to only include records which have the
birthday field set.

    :::python
    def validPerson(person):
      return person.valueForProperty_(\
        AddressBook.kABBirthdayProperty) is not None

    def bookFields(book):
      return [ personToFields(p) \
        for p in book.people() if validPerson(p) ]

I'm still in awe over how nicely the PyObjC does the translation behind
the scenes. The native python list constructs loop effortlessly across
the Objective C objects.

The next part in the story is to actually create the tuple with the
person's name and birthday. If you recall, this should look something
like:

    :::python
    {'date': 1977-08-04 12:00:00 GMT, 'name': u'Geoff Wilson'}

I've hidden this away in the `personToFields` function, with two
functions to get some details, as follows:

    :::python
    def personToFields(person):
      return {
        'date': getBirthday(person),
        'name': getPersonName(person)
        }

    def getPersonName(person):
      return person.valueForProperty_(\
        AddressBook.kABFirstNameProperty\
          ) + ' ' \
            + person.valueForProperty_(\
              AddressBook.kABLastNameProperty)

    def getBirthday(person):
      return person.valueForProperty_(\
        AddressBook.kABBirthdayProperty)

At this stage you should have enough code to be able to query your
Address Book. Python allows you to add the equivalent of a main function
to a source file. Similar to the Java usage, I've used this to write
quick test code to my module. Better would be to write unit test cases,
but this isn't an example of [TDD][].

Add the following to your code:

    :::python
    if __name__ == '__main__':
      print dateFields()

And then run the result:

    :::python
    $ python DateList.py
    [{'date': 2004-04-04 12:00:00 Australia/Melbourne, 'name': u'Test User'}]
    $

Note: if you don't have any records in Address Book, you won't see any
results.

The change to integrate this into the user interface is to update the
delegate to request the data from the `dateFields()` function. You also
need to add the appropriate import call:

    :::python
    from PyObjCTools import NibClassBuilder
    from DateList import dateFields

    NibClassBuilder.extractClasses('MainMenu')

    class DateListDelegate(NibClassBuilder.AutoBaseClass):
      def items(self):
        return dateFields()

The magical bit is that there is no need to re-compile and no need to
change the user interface. You should now see something like:

![Birthday list][]

The source code for the sample application from this tutorial is
available [here][].

  [Part 1]: http://www.pseudofish.com/blog/2005/05/13/part-1-creating-a-basic-cocoabindings-app-with-pyobjc/
  [PyObjC]: http://pyobjc.sourceforge.net/
  [Apple documentation]: http://developer.apple.com/documentation/UserExperience/Reference/AddressBook/ObjC_classic/Classes/ABPerson.html
  [TDD]: http://www.amazon.com/exec/obidos/ASIN/0321146530/qid=1116934788/sr=2-2/ref=pd_bbs_b_2_2/002-8975425-5740801
  [Birthday list]: /illustrations/2005-05DateList.jpg
  [here]: http://www.pseudofish.com/files/DateList-1.1.zip
