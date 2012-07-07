import httplib
from mock import Mock

from pyping.model import Monitor


def mock_opener_director(response_code=httplib.OK):
	"""Build a mock OpenerDirector instance.

	The returned instance will have an open method returning a response
	object that mimics the interface of urllib2's responses::

		>>> od = mock_opener_director()
		>>> url = 'http://google.com'
		>>> response = od.open(url)

		>>> od.open.assert_called_once_with(url)
		>>> httplib.OK == response.code
		True

		>>> response2 = mock_opener_director(httplib.NOT_FOUND).open('http://localhost/bogus')
		>>> httplib.NOT_FOUND == response2.code
		True

	"""

	mock_response = Mock(
		code = response_code
	)

	open = Mock(return_value=mock_response)

	opener_director = Mock(open=open)

	return opener_director


def test_valid_local_http_response_should_yield_positive():
	opener_director = mock_opener_director()
	monitor = Monitor('http://localhost:8000', opener_director=opener_director)

	response = monitor.ping()

	opener_director.open.assert_called_once_with('http://localhost:8000')

	assert response
	assert httplib.OK == response.response_code


def test_not_found_should_yield_negative():
	opener_director = mock_opener_director(response_code=httplib.NOT_FOUND)
	monitor = Monitor('http://localhost:8000/404.html', opener_director=opener_director)
	response = monitor.ping()

	assert not response
	assert httplib.NOT_FOUND == response.response_code


def test_valid_remote_http_response_should_yield_positive():
	opener_director = mock_opener_director()
	monitor = Monitor('http://google.com', opener_director=opener_director)
	response = monitor.ping()

	assert response
	assert httplib.OK == response.response_code
