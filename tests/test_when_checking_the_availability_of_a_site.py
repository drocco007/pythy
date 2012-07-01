import httplib

from pyping.model import Monitor


# for this to work, open a shell and run
#
#   python -m SimpleHTTPServer
#
# or fire up your favorite web server on port 8000

def test_valid_local_http_response_should_yield_positive():
	monitor = Monitor('http://localhost:8000')
	response = monitor.ping()

	assert response
	assert httplib.OK == response.response_code


def test_not_found_should_yield_negative():
	monitor = Monitor('http://localhost:8000/404.html')
	response = monitor.ping()

	assert not response
	assert httplib.NOT_FOUND == response.response_code


def test_valid_remote_http_response_should_yield_positive():
	monitor = Monitor('http://google.com')
	response = monitor.ping()

	assert response
	assert httplib.OK == response.response_code
