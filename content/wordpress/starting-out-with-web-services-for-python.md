Title: Starting out with web services for Python
Date: 2005-06-13 18:04
Author: gmwils
Category: Musings, Python

One of the things that I've been looking at is web services. So far,
I've played around with .NET, Java (Axis) and PHP for writing and
consuming them, however I wanted to be able to at least access them from
Python.

A quick web search didn't unearth a site which covered everything I was
interested in, so a bit more digging was required. The following
resources I've found useful so far:

-   [SOAP Web Services][] from Dive into Python. Covers pretty much
    everything, including WSDL.
-   [Python SOAP Libraries, Part 5][] from IBM's developerWorks. Good
    information on when things go bad. Also has some good references at
    the end.
-   [Python Web Services][]. A container site that includes both the
    SOAPpy and the ZSI web services code bases for Python.
-   [README for SOAPpy][]. Includes installation instructions and code
    examples

For now, I'm going to try out SOAPpy as it seems simpler. However, ZSI
appears to have better support for complex types in WSDL. Complex types
being the feature that tends to limit most WSDL tools.

As an example, here is a simple server:

    :::python
    import SOAPpy
    import os

    def systemInfo():
        return os.uname()

    server = SOAPpy.SOAPServer(('localhost', 8080))
    server.registerFunction(systemInfo)
    server.serve_forever()

The client is as easy as:

    :::python
    >>> import SOAPpy
    >>> proxy = SOAPpy.SOAPProxy('http://localhost:8080/')
    >>> proxy.systemInfo()[0]
    'Darwin'
    >>>

`os.uname()` returns an array of data, which is encoded into XML by the
server, and then decoded back into a Python array in the client. On the
wire, the actual data looks like:

    :::xml
    <SOAP-ENV:Body>
      <systemInfoResponse SOAP-ENC:root="1">
      <Result SOAP-ENC:arrayType="xsd:string[5]" xsi:type="SOAP-ENC:Array">
        <item>Darwin</item>
        <item>mayumi.local</item>
        <item>8.1.0</item>
        <item>Darwin Kernel Version 8.1.0: Tue May 10 18:16:08 PDT 2005;root:xnu-792.1.5.obj~4/RELEASE_PPC</item>
        <item>Power Macintosh</item>
      </Result>
      </systemInfoResponse>
    </SOAP-ENV:Body>

[Dive into Python][] has further information on how to obtain debugging
information, as well as an example of performing a Google search.

  [SOAP Web Services]: http://diveintopython.org/soap_web_services/index.html#soap.divein
  [Python SOAP Libraries, Part 5]: http://www-106.ibm.com/developerworks/webservices/library/ws-pyth17.html
  [Python Web Services]: http://pywebsvcs.sourceforge.net/
  [README for SOAPpy]: http://cvs.sourceforge.net/viewcvs.py/*checkout*/pywebsvcs/SOAPpy/README?rev=HEAD
  [Dive into Python]: http://diveintopython.org/soap_web_services/debugging.html
