.. |->| unicode:: U+02192 .. ->

pragmatic pytesting
===================

..

----


http://is.gd/pythy
==================

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

Installation:

    .. code-block:: bash

        $ virtualenv my_project
        $ cd my_project ; . bin/activate
        $ pip install pytest pytest-cov mock
        $ mkdir my_package ; mkdir tests

Fire it up:

    .. code-block:: bash

        $ py.test tests/


----


Test Layout: Module Inline
==========================

.. code-block:: python

    def get_random_number():
        import webbrowser ; webbrowser.open("http://xkcd.com/221/")

        return 4

    def test_get_random_number():
        assert 4 == get_random_number()


----

Inline Special Case: doctests!
==============================

    .. code-block:: python

        def foo():
            """Foos

                >>> foo()
                'bar'
            """
            return 'bar'


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

*This layout simplifies coverage testing*


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

..


----

Our First Run
=============

::

    monitor('http://localhost:8000')

NB: for this to work, you need a running web server::

    $ python -m SimpleHTTPServer


----

Problems
========

::

    monitor('http://google.com')


----

Revelation
==========

``urlopen`` isn't broken.


----

What We Actually Care About
===========================


Presenter notes
===============

    behavior on: successful response, failed response, successful response
    with good/bad text, timeout

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

----


Testing the Improved Monitor with Mock
======================================

..

----

Success
=======

..

----

Failure
=======

..

----

Timeout
=======

..

----

New Feature: Desired Text
=========================

..

----

Making Valid Results "Truthy"
=============================

..

----

Gotcha Covered
==============

..


----

the inevitable question
=======================

.. class:: mat pull-right
.. image:: images/nose_fabulous.jpg
