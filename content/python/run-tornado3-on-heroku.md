Title: Run Tornado 3 on Heroku
Date: 2013-05-01
Author: gmwils
Summary: How to get Tornado 3 deployed on Heroku
status: draft

Notes from getting Tornado setup and working on Heroku.

## Tornado 3

Follow the instructions in the documentation
[overview](http://www.tornadoweb.org/en/stable/overview.html).

I've found the Tornado docs to be very helpful. The
[code](https://github.com/facebook/tornado) is clearly written should you be
curious on how something works.

## Python 3

To enable Python 3 on Heroku, it is a simple matter of creating a runtime.txt
with the version you want:

    $ cat runtime.txt
    python-3.3.1

For more details, see
[here](https://devcenter.heroku.com/articles/python-runtimes).

## Gunicorn

Getting Tornado to run with [Gunicorn](http://gunicorn.org/) takes a bit of
playing around.
[This](https://groups.google.com/forum/?fromgroups=#!topic/python-tornado/tTzZvHaLfb0)
thread helped get me going.

By using the tornado runner, you get to keep all of Tornado's async features,
while letting gunicorn run multiple instances for you.

My Procfile ended up with:

    web:      gunicorn -k tornado -b 0.0.0.0:$PORT -w 4 main

I also added gunicorn to requirements.txt. I needed to make some changes to
how my application was started too. As an example see
[here](https://github.com/gmwils/cihui/blob/master/main.py).

The main thing is for there to be a variable called application. You could
call it something else (eg. app) and then would need to call it explicitly in
the Procfile.

    web:      gunicorn -k tornado -b 0.0.0.0:$PORT -w 4 main:app

This setup allows you to run multiple instances of Tornado, to allow for some
to block if needed.

## PostgreSQL

The database of choice for Heroku is PostgreSQL, however Tornado doesn't ship
with default drivers for it.

I've found [Momoko](http://momoko.61924.nl/en/latest/tutorial.html) to work
really well. It is a wrapper around [Psycopg2](http://www.initd.org/psycopg/),
with both sync and async support.

