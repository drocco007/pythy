__author__ = 'Daniel J. Rocco'

import pytest


def test_simple_pass():
	"""The simplest passing test"""
	pass


def test_simple_assertions():
	"""Demonstrates passing tests that use assert"""
	assert True
	assert [1]
	assert dict(pytest='awesome')


def test_expected_exception():
	"""Demonstrates pytest's raises context manager"""

	with pytest.raises(ZeroDivisionError):
		1/0

	with pytest.raises(IOError):
		open('/some/bogus/file.txt')


def doctest_example():
	"""pytest can also run doctests

	notice this function is not a test itself, but its docstring contains
	doctests::

		>>> doctest_example()
		"I came from a doctest!  Isn't that great?"
		>>> 1 + 1
		2

	pytest's default configuration is to run doctests in any files
	matching the glob pattern ``text*.txt``.  To get it to run doctests
	in module document comments like this one, pass the
	``--doctest-modules`` flag.
	"""
	return 'I came from a doctest!  Isn\'t that great?'
