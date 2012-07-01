__author__ = 'Daniel J. Rocco'

def test_simple_fail():
	assert False


def test_simple_fail_with_message():
	assert False, 'Snap, something went wrong...'


def test_uncaught_exceptions_fail_test():
	open('this is not the file you are looking for...')
