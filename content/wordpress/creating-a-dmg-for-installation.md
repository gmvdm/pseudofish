Title: Creating a .dmg for installation
Date: 2005-07-13 20:29
Author: gmwils
Category: apple

Having been talked out of making an installer, I still wanted to be able
to automate the creation of a .dmg file for easy deployment.
Fortunately, this is very simple to do if you don't want the .dmg to do
much.

The short version is:

    :::shell
    % hdiutil create -srcfolder dist/[app name].app [app name].dmg

With [app name] replaced with the name of your application. Obviously,
you need to do a proper build of your Python application, the
symbolically linked version isn't good enough.

For example, the Date List sample app can be deployed with:

    ::: shell
    % rm -rf dist
    % python setup.py py2app
    % hdiutil create -srcfolder dist/Date\ List.app Date\ List.dmg

There are a range of features that are worth adding to a .dmg that is
used to deploy software. These include things like background images,
license agreements and auto opening the disk image.

This is something to investigate at a future point. The [buildDMG][]
script seems to be a good starting point, with the [source][] of
[Adium][] providing a good example of how to build one.

  [buildDMG]: http://www.objectpark.org/buildDMG.html
  [source]: http://trac.adiumx.com/wiki/GettingAdiumSource
  [Adium]: http://www.adiumx.com/
