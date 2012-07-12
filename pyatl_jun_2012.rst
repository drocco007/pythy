.. |->| unicode:: U+02192 .. ->

.. class:: show_title huge

pragmatic pytesting

Daniel J. Rocco, Ph.D.

----


http://is.gd/pythy
==================

Presenter notes
===============

..

----


def pytest
==========

.. code-block:: python

    def pytest():
        """A mature, full-featured python test runner and tool-suite

        *   easy to write tests, easy to run, easy to maintain
        *   supplied tools address most common testing needs
        *   orthogonal architecture provides advanced features
            with minimal intrusion"""

        pytest.main()


----


Simplest Passing Test
=====================

    .. code-block:: python

        def test_simple_pass():
            """The simplest passing test"""
            pass

----

assert is_your_friend
=====================

    .. code-block:: python

        def test_simple_assertions():
            """Demonstrates passing tests that use assert"""
            assert True
            assert [1]
            assert dict(pytest='awesome')


----

assert not your_enemy
=====================

    .. code-block:: python

        def test_negative_assertions():
            """Demonstrates passing tests that use negated assertions"""
            assert not False
            assert not []
            assert not dict()

----

Simplest Failing Test
=====================

    .. code-block:: python

        def test_simple_fail():
            assert False


        def test_simple_fail_with_message():
            assert False, 'Snap, something went wrong...'

----

Caught Off Guard
================

    .. code-block:: python

        def test_uncaught_exceptions_fail_test():
            open('this is not the file you are looking for...')

----

Expect the Exceptional
======================

    .. code-block:: python

        def test_expected_exception():
            """Demonstrates pytest's raises context manager"""

            with pytest.raises(ZeroDivisionError):
                1/0

            with pytest.raises(IOError):
                open('/some/bogus/file.txt')


----

We Have Liftoff!
================

.. class:: row
..

    .. class:: pull-left
    ..

        Installation:

            .. code-block:: bash

                $ virtualenv my_project
                $ cd my_project ; . bin/activate
                $ pip install pytest pytest-cov mock
                $ mkdir my_package ; mkdir tests

        Fire it up:

            .. code-block:: bash

                $ py.test tests/

    .. class:: pull-right mat
    .. image:: images/rocket.jpg

----


Test Layout: Module Inline
==========================

    .. code-block:: python

        def get_random_number():
            """Algorithm courtesy of http://xkcd.com/221/"""

            return 4


        def test_get_random_number():
            assert 4 == get_random_number()

----

Inline Special Case: doctests!
==============================

    .. code-block:: python

        def will_it_blend(thing):
            """Will the thing blend?

                >>> will_it_blend('a car')
                True
                >>> will_it_blend('tomato juice')
                False
            """
            return thing == 'a car'


    Invoke pytest with the ``--doctest-modules`` switch

----


Test Layout: Sidecar
====================

    ::

        package/

            __init__.py
            module.py
            ...

            test_package.py
            test_package_module.py
            ...


----


Test Layout: Quarantine
=======================

    ::

        proj/
            package/
                __init__.py
                foo_bar_baz.py
                ...

            package2/
                ...

            tests/
                test_foo_bar_baz.py

            setup.py

*This layout simplifies coverage testing*


----

.. image:: images/seal.png
    :align: center

----

By Way of Example
=================

Wormly clone; basic requirements:

    *   periodically ping a URL
    *   check for valid response code, presence or absence of certain text
    *   timeout | bad response | bad text |->| failure
    *   send notification on failure
    *   track response history

----

"It's Only a Model"
===================

    .. class:: mat
    .. image:: images/oh_no_uml.png
        :align: center


----

Monitor v0.1
============

    .. code-block:: python
    
        class Response(object):
            """Abstraction around urlopen's various response types"""
            ...

        class Monitor(object):
            def __init__(self, url):
                self.url = url

            def ping(self):
                try:
                    url_response = urlopen(self.url)
                    response = Response(response=url_response)
                except IOError, e:
                    response = Response(exception=e)

                return response

----

Our First Test Run
==================

    .. code-block:: python

        def test_valid_local_http_response_should_yield_positive():
            monitor = Monitor('http://localhost:8000')
            response = monitor.ping()

            assert response
            assert httplib.OK == response.response_code

    NB: for this to work, you need a running web server:

        ::

            $ python -m SimpleHTTPServer

    which lets us know that we have

----

Problems
========

----

Revelation: ``urlopen`` isn't broken.
=====================================

Presenter Notes
===============

..

----

What We Actually Care About
===========================

Presenter Notes
===============

..  this section will be hidden in the output; here to keep landslide
    from complaining

----

What We Actually Care About
===========================

Given a mechanism for opening URLs,

When I check the availability of a given URL,

*   good response (e.g. 200) should yield success response
*   timeout should yield failure response
*   bad response code (e.g. 404) should yield failure response
*   good response with bad text in the response should yield failure response

Presenter notes
===============

    behavior on: successful response, failed response, successful response
    with good/bad text, timeout

    meta-answer: need to think carefully about what you are testing and why

----

Testability and a Little Dependency Injection
=============================================

DI pattern core idea: function's dependencies should appear in its signature

    .. code-block:: python

        def dependencies_go(here=True):

            dependencies = not here

Presenter Notes
===============

core idea: pass function's dependencies to it on call

rationale:

    *   communication: function communicates its dependencies in its
            signature, rather than having implicit dependencies scattered
            throughout its implementation
    *   isolation: DI fn is loosely coupled to the rest of the system: deps
            flow to it from caller
    *   testability: much easier to provide alternative test implementations
            of deps

----

Non-DI Monitor
==============

    .. code-block:: python

        class Monitor(object):
            def __init__(self, url):
                self.url = url

            def ping(self):
                try:
                    url_response = urlopen(self.url)
                                   ^^^^^^^
                    ...

Presenter Notes
===============

Monitor has a hard dependency on urlopen that makes it difficult to test.

* What happens if the network is down?
* How can I easily test error codes like 401 & 403?
* What if I need non-default behavior, e.g. NTLM auth?

----

Improving Monitor with DI
=========================

    .. code-block:: python

        class Monitor(object):
            open = staticmethod(urlopen)

            def __init__(self, url, opener_director=None):
                self.url = url

                if opener_director:
                    self.open = opener.open


            def ping(self):
                try:
                    url_response = self.open(self.url)
                    ...

Presenter Notes
===============

Using dependency injection allows us to break the hard dependency on urlopen,
although for convenience it is still the default.

Advantages:

*   By default, works exactly as it used to
*   Monitor is now more flexible: I can use any implementation that conforms
    to OpenerDirector's interface
*   For testing, I can pass mock objects that provide responses mimicking
    real scenarios without actually talking over the network

----

Great!  Er, how does that help?
===============================

Presenter notes
===============

.. this section intentionally left (non)blank

----

``old_dog.tricks.append(...)``
==============================

.. code-block:: python

    # Basic HTTP Auth
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(...)
    opener = urllib2.build_opener(auth_handler)

    Monitor('http://super.secret.com', opener)



    # Custom user agent
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    Monitor('http://abolish-all-robots.org', opener)



----

Don't Mock Me
=============

Power tool: Michael Foord's `Mock <http://www.voidspace.org.uk/python/mock/>`_ library

Mock instances are callable:

    .. code-block:: python

        >>> from mock import Mock
        >>> mock_fn = Mock(return_value=42)
        >>> mock_fn()
        42

They provide useful information to your tests:

    .. code-block:: python

        >>> mock_fn.assert_called_once_with()

----

Don't Mock Me Again
===================

By default, accessing an attribute on a Mock yields a new Mock, making
object mocking trivial:

    .. code-block:: python

        >>> mock_obj = Mock()
        >>> isinstance(mock_obj.foo, Mock)
        True

        >>> mock_obj.foo.return_value = 'I\'m a return value!'
        >>> mock_obj.foo('I\'m an argument!')
        "I'm a return value!"

        >>> mock_obj.foo.assert_called_once_with('I\'m an argument!')

----

Mocking ``build_opener``
========================

OpenerDirector's ``open`` method |->| response object

``response.code`` |->| HTTP status


----

Mocking ``build_opener``
========================

    .. code-block:: python

        def mock_opener_director(response_code=httplib.OK):
            """Build a mock OpenerDirector instance."""

            mock_response = Mock(code=response_code)

            open = Mock(return_value=mock_response)

            opener_director = Mock(open=open)

            return opener_director

----

Success
=======

    .. code-block:: python

        def test_valid_local_http_response_should_yield_positive():
            opener_director = mock_opener_director()
            url = 'http://localhost:8000'
            monitor = Monitor(url, opener_director=opener_director)

            response = monitor.ping()

            opener_director.open.assert_called_once_with(url)

            assert response
            assert httplib.OK == response.response_code

----

Failure
=======

Or, rather, failing to fail...

    ::

        def test_not_found_should_yield_negative():
            opener_director = mock_opener_director(
                                  response_code=httplib.NOT_FOUND
                              )
            monitor = Monitor('http://localhost:8000/404.html',
                              opener_director=opener_director)
            response = monitor.ping()

        >       assert not response
        E    assert not <pyping.model.Response object at 0x...>

----

How does this thing work again?
===============================

    .. code-block:: python

        def mock_opener_director(response_code=httplib.OK):
            mock_response = Mock(code=response_code)

            open = Mock(return_value=mock_response)
            ...

.. class:: row
..

    .. class:: mat pull-left
    .. image:: images/head_scratcher.jpg

    .. class:: narrow column pull-right
    ..

        Wait, that isn't right!

        What about a ``response_code`` that's an error?

----

For realz this time
===================

    .. code-block:: python

        def mock_opener_director(response_code=httplib.OK):
            mock_response = Mock(code=response_code)

            def _side_effect(*args, **kw):
                if response_code < 300:
                    return DEFAULT
                else:
                    error = IOError()
                    error.code = response_code
                    raise error

            open = Mock(return_value=mock_response,
                        side_effect=_side_effect)

            opener_director = Mock(open=open)

            return opener_director

----

Other goodies
=============

.. class:: row
..

    .. class:: column nobullets pull-left

    *   stop after the first failure::

        $ py.test -x ...

    *   fire up ye olde debugger on failure::

        $ py.test --pdb ...


    .. class:: column nobullets pull-left

    *   suppress output capture::

        $ py.test -s ...


    *   gotcha covered:

        .. code-block:: bash

            $ py.test --cov pyping \
                      --cov-report=html \
                      tests/


----

.. class:: row
..

        .. class:: huge nobullets pull-left compact

        * the
        * inevitable
        * question

        .. class:: mat pull-left
        .. image:: images/nose_fabulous.jpg


----

``import sys; sys.exit()``
==========================
