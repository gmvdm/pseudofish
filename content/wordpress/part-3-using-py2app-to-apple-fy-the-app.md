Title: Part 3 - Using py2app to Apple-fy the app
Date: 2005-05-29 12:52
Author: gmwils
Category: Musings, Python

`py2app` provides a few more things than just packaging up the code into
a bundle. To make the app more of a first class citizen in the Apple
world, I'm going to add nice things like an icon, an About box and a
proper name.

</p>

Apple provides quite a nice way of specifying all of this information in
a .plist file and `py2app` is quite happy to make use of it. As the
example, I'm going to take the list of birthdays made in parts [1][] and
[2][] and improve it without changing the code, well not too much.

</p>

First step is to let `py2app` know where to find our .plist file. This
involves a change to `setup.py` by creating an options entry to give the
name of the .plist file:

<p>
    setup(    data_files=['English.lproj'],    app=['main.py'],    options=dict(py2app=dict(plist='Info.plist')))

</p>

Everything else is accomplished by adding in entries to the `Info.plist`
file. According to the Mac OS X '[Runtime Configuration: Guidelines For
Configuring Applications][]' guide, there are a bunch of keys that need
to be set as a minimum. I'm going to go through each key and what they
actually *do* for your app.

To give my application a name, other than `main.app`, it is a matter of
setting the `CFBundleName` property in the `Info.plist` file. There is a
bit of boilerplate required which does nice XML things about specifying
schemas and encodings. I've also added the package type in for now, with
`APPL` representing an Application.

</p>

<p>
    <?xml version='1.0' encoding='UTF-8'?><!DOCTYPE plist PUBLIC '-//Apple Computer//DTD PLIST 1.0//EN''http://www.apple.com/DTDs/PropertyList-1.0.dtd'><plist version='1.0'><dict>    <!-- Used by py2app to generate application bundle -->    <key>CFBundleName</key>    <string>Date List</string>    <!-- Package type is an Application -->    <key>CFBundlePackageType</key>    <string>APPL</string></dict></plist>

</p>

At this point, building the application will result in the name of the
application bundle being set correctly. Additionally, the application
name will appear in the menu bar and in the About box. If you do a *Get
Info* on the application bundle, it also shows up as an Application.

</p>

There are some other fields that Mac OS X will set for you in the About
box if you fill in the appropriate properties. For example:

</p>

<p>
        <!-- Version number - appears in About box -->    <key>CFBundleShortVersionString</key>    <string>1.2</string>    <!-- Build number - appears in About box -->    <key>CFBundleVersion</key>    <string>12</string>    <!-- Copyright notice - apears in About box -->    <key>NSHumanReadableCopyright</key>    <string>© Geoff Wilson 2005</string>

</p>

The About box is looking pretty good at this point, but for one key
thing. That default icon simply has to go. Fortunately, it is as simple
as specifying the appropriate property, and putting the icon file in the
`English.lproj` directory.

</p>

<p>
        <key>CFBundleIconFile</key>    <string>DateList</string>

</p>

All well and good, but I had absolutely no idea how to create an icon
for Mac OS X. I'd gone through enough pain trying to get the `favicon`
working for this site. Mac OS X icons looked much tricker. Fortunately,
Mac OS X comes with its own tool for building icons, called *Icon
Composer*. It lives under `/Developer/Applications/Utilities`

</p>

Icon development is something that you should take some time to consider
for a real application. There is a good [article][] at the O'Reilly
site, and also some information from [Apple][]. The short version is to
drag an image into *Icon Composer* and save the results.

</p>

The icon file will be saved with an .icns extension, but there doesn't
seem to be a need to worry about that in the property file. In the
interests of avoiding graphic design for a minute, I used the banner
image from this site. This has the downside of making a solid square,
but it means I can avoid Photoshop for a bit longer.

</p>

After re-building the application (to copy the icon file to the bundle),
my icon turns up in all sorts of useful places like the About box, the
Dock and the Finder.

</p>

![About box][]

There are a few more properties that are required to be set in the
property file. The `CFBundleIdentifier` property is used to uniquely
identify your application. The remaining properties, I'm not too sure as
to where they are used, but they seem obvious enough to set values for.
English is my development environment and the executable and bundle
display name are set to the bundle name so that everything matches.

</p>

<p>
        <!-- Globally unique identifier -->    <key>CFBundleIdentifier</key>    <string>com.pseudofish.DateList</string>    <key>CFBundleDevelopmentRegion</key>    <string>English</string>    <key>CFBundleExecutable</key>    <string>Date List</string>    <key>CFBundleDisplayName</key>    <string>Date List</string>

</p>

The complete Info.plist is included with the updated [example][]. Now
replete with a proper name, dock icon and an About box.

</p>

  [1]: http://www.pseudofish.com/blog/2005/05/13/part-1-creating-a-basic-cocoabindings-app-with-pyobjc/
  [2]: http://www.pseudofish.com/blog/2005/05/24/part-2-using-address-book-and-making-an-app/
  [Runtime Configuration: Guidelines For Configuring Applications]: http://developer.apple.com/documentation/MacOSX/Conceptual/BPRuntimeConfig/Tasks/ConfigApplications.html
  [article]: http://www.macdevcenter.com/pub/a/mac/2001/05/24/aqua_design.html?page=1
  [Apple]: http://developer.apple.com/documentation/UserExperience/Conceptual/OSXHIGuidelines/index.html
  [About box]: /illustrations/2005-05About.jpg
  [example]: /files/DateList-1.2.zip
