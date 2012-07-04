
===================
pragmatic pytesting
===================

This is a support project for the July 2012 PyAtl Meetup talk *pragmatic
pytesting*.  It contains

    #.  basic tests demonstrating pytest features (``tests/examples``)
    #.  a tested example project
    #.  the slides for the talk


The Project
===========

*pyping* is a nascent `Wormly <http://www.wormly.com>`_ clone providing
monitoring services for web applications.  Imagine a system that allows
you to periodically ping a given URL, perhaps checking for the presence
or absence of certain text, and notifies you if something goes wrong.

Hopefully it is obvious that the purpose of this project is *not* to
actually build a Wormly clone but rather to provide a demonstration
scaffold that is real enough to show how you might test an actual
project.


HOWTO
=====

    *   install pytest::

        $ virtualenv pyping
        $ cd pyping ; . bin/activate
        $ pip install pytest pytest-cov mock

    *   run the tests::

        $ py.test tests/

    *   stop after the first failure::

        $ py.test -x tests/

    *   drop into the debugger on failure::

        $ py.test --pdb tests/

    *   generate a coverage report for the ``pyping`` package and output
        the results to the terminal and an HTML file::

        $ py.test --cov pyping --cov-report html --cov-report term tests

    *   turn the presentation source into a slide show::

        $ pip install landslide
        $ landslide -t theme pyatl_jun_2012.rst

