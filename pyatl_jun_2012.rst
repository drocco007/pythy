
===================
pragmatic pytesting
===================

----------------------
Daniel J. Rocco, Ph.D.
----------------------

.. :author: Daniel J. Rocco, Ph.D.

----


For Those of You Following Along at Home
========================================

http://is.gd/pythy
------------------

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


Whetting Your Appetite
======================

Simplest Passing Test
---------------------

.. code-block:: python

    def test_simple_pass():
        """The simplest passing test"""
        pass


    def test_simple_assertions():
        """Demonstrates passing tests that use assert"""
        assert True
        assert [1]
        assert dict(pytest='awesome')


Simplest Failing Test
---------------------

.. code-block:: python

    def test_simple_fail():
        assert False


    def test_simple_fail_with_message():
        assert False, 'Snap, something went wrong...'




----


Exceptions
==========

.. code-block:: python

    def test_uncaught_exceptions_fail_test():
        open('this is not the file you are looking for...')

    def test_expected_exception():
        """Demonstrates pytest's raises context manager"""

        with pytest.raises(ZeroDivisionError):
            1/0

        with pytest.raises(IOError):
            open('/some/bogus/file.txt')


----


We Have Liftoff!
================

.. code-block:: bash

    $ virtualenv my_project
    $ cd my_project ; . bin/activate
    $ pip install pytest pytest-cov mock
    $ mkdir my_package ; mkdir tests


----


Test Layout: Inline
===================

.. code-block:: python

    def foo():
        pass

    def test_foo():
        pass


Special case: doctests!

.. code-block:: python

    def foo():
        """Foos

            >>> foo()
            'bar'
        """
        return 'bar'


----


Test Layout: Sidecar
====================


----


Test Layout: Quarantine
=======================

.. code-block:: python

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
