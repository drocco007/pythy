from datetime import datetime
from urllib2 import urlopen


xor = lambda a, b: bool(a) ^ bool(b)


class Response(object):
	exception = None
	response = None

	def __init__(self, response=None, exception=None):
		if not xor(response, exception):
			raise ValueError('Must provide either a response or an exception')

		self.response = response
		self.exception = exception
		self.created = datetime.now()

	@property
	def response_code(self):
		if self.response:
			return self.response.code

		# Michael Foord's recipe, http://www.voidspace.org.uk/python/articles/urllib2.shtml
		if hasattr(self.exception, 'reason'):
			return self.exception.reason
		else:
			return self.exception.code

	def __nonzero__(self):
		return bool(self.response)


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
