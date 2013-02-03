Title: Using Qt with Microsoft VC++ Express
Date: 2006-12-14 15:42
Author: gmwils
Category: Technology

[Qt][] is a happy little framework that runs on pretty much anything
from Windows to embedded Linux. Most of my experience with it has been
on unix variants or on Mac OS X.

</p>

I thought I'd try it out under Windows, and to make things interesting,
I would use Visual C++ Express Edition as the C++ compiler. Trolltech's
website [states][] that it is possible, but not details as to how (at
least not that I found). My aim is not install cygwin or the full Visual
Studio package.

</p>

*Warning*: This is a strange configuration. If you want to use Qt for
open source development on Windows, just download the .exe from [here][]
and you'll get g++ included as part of MinGW. If you want to use Qt for
commercial development, then the full Visual Studio integration is
highly recommended.

</p>

Qt (commercial) is integrated into Visual Studio, however the Express
version of VC++ is limited so that it won't play nicely with normal
plugins. The main reason to use VC++ Express is for its command line
tools.

</p>

<u>Step 1</u> - Install Qt.

</p>

I installed the Qt commercial version built for VS2005. This seems to
work just fine with VC++ Express.

</p>

This version Qt is available under license from Trolltech and is also
available for a trial period. See [here][Qt] for more details.

</p>

<u>Step 2</u> - Install Visual C++, Express Edition.

</p>

VC++ Express can be downloaded from [here][1].

</p>

Run the installer and say yes to everything.

</p>

At this point you can use C++ to make .NET applications. To be able to
create native applications you need the Platform SDK.

</p>

<u>Step 3</u> - Install Platform SDK.

</p>

[This][] MSDN article explains how to get the Platform SDK to work with
VC++ Express.

</p>

Basically, download the SDK from [here][2] and install.

</p>

<u>Step 4</u> - Mess with the environment.

</p>

Edit the qtvars.bat file (in `C:\Qt\4.2.2\bin`) so that the `call` to
`vsvars32.bat` is outside an `if` statement.

</p>

The `if` statements check for the normal Visual Studio install, but miss
the Express version.

</p>

It is useful if you add `C:\Qt\4.2.2\bin` to your path, as then you can
call the qtvars.bat script from the command line.

</p>

Add the following variable to your environment:

</p>
<p>
    QTDIR=C:\Qt\4.2.2\bin

</p>

<u>Step 5</u> - Try it out.

</p>

Make a new directory and create a file called `hello.pro` with the
following:

</p>
<p>
    TEMPLATE = appSOURCES = main.cpp

</p>

Create a file called `main.cpp` with the following:

</p>

<p>
    #include int main( int argc, char *argv[] ) {    QApplication app( argc, argv );    QLabel *helloLabel = new QLabel( "Hello World" );    helloLabel->show();    return app.exec();}

</p>

From the command line run the following commands:

</p>

<p>
    c:\hello>qtvars...c:\hello>qmake...c:\hello>nmake...c:\hello>release\hello.exe

</p>

You should now see a very simple application that consists of a single
label saying "Hello World". Additionally, you also have a full Qt
development environment that is substantially more useful than
`hello.exe`.

</p>

  [Qt]: http://www.trolltech.com/products/qt/
  [states]: http://www.trolltech.com/developer/notes/compilers/vcpp
  [here]: 
  [1]: http://msdn.microsoft.com/vstudio/express/visualc/download/
  [This]: http://msdn.microsoft.com/vstudio/express/visualc/usingpsdk/
  [2]: http://www.microsoft.com/downloads/details.aspx?FamilyId=0BAF2B35-C656-4969-ACE8-E4C0C0716ADB
