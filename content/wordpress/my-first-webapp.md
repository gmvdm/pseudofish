Title: My First WebApp
Date: 2007-03-25 16:07
Author: gmwils
Category: Haskell, Musings, Python, Technology

There are lots of technologies that I have been investigating recently,
with the intent of building something useful. However, it's hard to
figure out if my plan makes sense without trying. So I am going to build
a very simple application.

The specification looks like:

<p>
> <font color="#555555">The application shall allow the user to send
> email notes to themselves</font>

</p>
I often email short notes to myself as reminders or to capture short
pieces of information. The number of steps involved in doing this is
[too many][]. I have to address the email, set a subject, navigate one
of many email clients and then send. I want to IM myself and have it
turn up as email.

My design for building this is a little bit more complex than it really
needs to be. This is because the application is an excuse to try
building a platform.

There are four pieces:

1.  Taskbar applet to send mail
2.  Web application to send mail
3.  Web service to receieve send mail request
4.  Application service to send mail

</p>
The task bar applet is the easy part (see [QSystemTrayIcon][]). That
will be built, initially for Windows, using Qt. If I'm enthusiastic, it
may support RTF and HTML email as well as unicode text.

The web application, likely to be built last, will use [django][]. I'm
considering Ruby on Rails, but given I already know python and django
provides sufficient functionality, it is my likely choice.

The web service will be built using the same web framework as the web
application. I am trying to reduce the number of technologies a little
bit.

The aims of the web service:

-   Provide a publically accessible API.
-   To allow for a flexible URL mapping scheme
-   To provide a REST style API.
-   To easily provide different data formats (XML, JSON).

</p>
The application service will be built using [Haskell][]. It will be kept
as an internal process. It will likely be built using a web service as
well, but using [JSON][] as the transport. I am choosing Haskell mainly
to explore options.

After my recent foray into Lisp, I am confident I could build the
application service using Lisp, but would prefer to use Haskell. This is
partially to avoid paying license fees to Allegro, but mostly as I
prefer having the type system of Haskell available. The architecture
will allow me to swap back-ends if needed.

That is the plan. Progress and learnings should trickle in over the
coming months.

<u>Note</u>: This is an exercise in playing with technology. There is no
plan for providing this as a production level service.

  [too many]: http://daringfireball.net/2007/03/deal_with_it
  [QSystemTrayIcon]: http://doc.trolltech.com/4.2/qsystemtrayicon.html#details
    "QSystemTrayIcon"
  [django]: http://www.djangoproject.com/ "Django Project"
  [Haskell]: http://haskell.org/ "Haskell"
  [JSON]: http://json.org/ "JSON"
