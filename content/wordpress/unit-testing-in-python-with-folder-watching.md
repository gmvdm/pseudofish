Title: Unit testing in Python with folder watching
Date: 2012-03-14 05:09
Author: gmwils
Category: Python

Unit testing is good. Running unit tests manually is annoying.

</p>

Rspec has a great addition in [autospec][], which automatically re-runs
specs that are changed or have the associated code changed. This model
of working has a long history in the ruby community, with [autotest][].

</p>

I wanted a similar thing for python/[nose][], but hadn't had much luck.

</p>

The solution is [py.test][], with some plugins added.

</p>

This was suggested to me at the [Stockholm Python user group][], and I
am very grateful. My testing life is now much simpler.

</p>

To get started, try something like:

</p>

<p>
    $ sudo pip install pytest pytest-xdist pytest-cov

</p>

The simple way to get started is to watch your tests folder:

</p>

<p>
    py.test -f test/

</p>

Now as you change files, the relevant tests will automatically be
re-run. Perfect to display on that second monitor.

</p>

As I was working on some legacy code, I was looking to improve the test
coverage, so wanted to see how that was going with [pytest-cov][]:

</p>

<p>
    py.test -f --cov package.name test/

</p>

Adding the *package.name* for your main package means you won't generate
coverage for libraries you are using. Makes the output simpler.

</p>

Still not quite happy, it wasn't showing me which lines I needed
coverage on. No problem:

</p>

<p>
    py.test -f --cov package.name --cov-report term-missing test/

</p>

For comparison, here is how to get similar results from nose, but
without watch support:

</p>

<p>
    nosetests test/nosetests --with-coverage --cover-erase --cover-package=package.name test/

</p>

One hurdle I had with py.test was working with [Twisted][] based
test-cases. You need to ensure that you use a version of py.test later
than 2.0. Debian squeeze does not package this by default, so use pip to
install.

</p>

The annoyance is if you change the code so it doesn't terminate. This
still needs a context switch to kill off the tests and re-run. Keeps me
focused on getting it right the first time.

</p>

[pytest-xdist][] includes lots of really cool options, such as
distribution of tests across multiple cores, versions, hosts and
platforms.

</p>

I've since discovered this [comprehensive summary][] of the options
available. I'm happy I found this after selecting [py.test][], or I'd
still be stuck in evaluation mode rather than writing code.

</p>

*Update*: check out [sniffer][] if you want a more generic watcher
framework.

</p>

  [autospec]: http://lostechies.com/derickbailey/2010/05/03/zentest-autospec-is-an-rspec-tdder-s-best-friend/
  [autotest]: http://nubyonrails.com/articles/autotest-rails
  [nose]: http://readthedocs.org/docs/nose/en/latest/
  [py.test]: http://pytest.org/latest/
  [Stockholm Python user group]: http://www.meetup.com/pysthlm/
  [pytest-cov]: http://pypi.python.org/pypi/pytest-cov
  [Twisted]: http://twistedmatrix.com/trac/
  [pytest-xdist]: http://pypi.python.org/pypi/pytest-xdist
  [comprehensive summary]: http://wiki.python.org/moin/PythonTestingToolsTaxonomy
  [sniffer]: http://pypi.python.org/pypi/sniffer
