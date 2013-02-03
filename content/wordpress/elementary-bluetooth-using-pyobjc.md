Title: Elementary Bluetooth using PyObjC
Date: 2006-03-28 22:49
Author: gmwils
Category: Apple, Cocoa, Musings, Python

Bluetooth connectivity to devices is supported on Mac OS X using Cocoa
APIs, so is possible to access from Python. Bluetooth itself opens up a
large body of knowledge that I am only starting to investigate.

</p>

This article outlines some basics for using Bluetooth in Python.

</p>

Bluetooth access is achieved through two frameworks, `IOBluetooth` and
`IOBluetoothUI`. Neither of these are included in PyObjC by default, so
a basic wrapper class makes life easier. (see the [PyObjC docs][])

</p>

Add the following to `IOBluetooth.py`:

</p>

<p>
    import objc as _objc_objc.loadBundle('IOBluetooth', globals(),   bundle_path=u'/System/Library/Frameworks/IOBluetooth.framework')

</p>

The loadBundle pattern is very useful, and allows the classes from any
Objective C framework to be loaded into the PyObjC bridge. By putting it
into a separate Python module, usage becomes less painful.

</p>

For example, the most recent device is:

</p>

<p>
    >>> from IOBluetooth import *>>> devs = IOBluetoothDevice.recentDevices_(1)>>> devs[0].getNameOrAddress()u'gmwils 6600'>>> devs[0].isConnected()1>>> 

</p>

In this case, my Nokia 6600 is still connected in AddressBook.

</p>

To create a new connection to a device, Apple provides access to their
user interface for Bluetooth management. It is strongly recommended that
these controls are used to provide consistency for the user and detailed
error handling.

</p>

For example, selecting a service from a device with a dialog:

</p>

<p>
    >>> from IOBluetoothUI import *>>> browser = IOBluetoothServiceBrowserController.serviceBrowserController_(0)>>> browser.runModal()-1000>>> results = browser.getResults()>>> results[0].getServiceName()u'Bluetooth Serial Port'>>> 

</p>

Note: you will need a `IOBluetoothUI` wrapper, similar to the
`IOBluetooth` wrapper from earlier.

</p>

Useful documentation links:

</p>

-   [Apple Bluetooth documents][]
-   [Apple Bluetooth-dev mailing list][]
-   [Bluetooth specifications][]

</p>

  [PyObjC docs]: http://pyobjc.sourceforge.net/doc/wrapping.php
  [Apple Bluetooth documents]: http://developer.apple.com/documentation/DeviceDrivers/Bluetooth-date.html#//apple_ref/doc/uid/TP30000423-TP30000490
  [Apple Bluetooth-dev mailing list]: http://lists.apple.com/archives/Bluetooth-dev/
  [Bluetooth specifications]: https://www.bluetooth.org/spec/
