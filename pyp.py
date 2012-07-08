from time import sleep
from pyping.model import Monitor

DEFAULT_TIMEOUT = 5

urls = ['http://google.com', 'http://localhost:8000']


class Hub(object):
	observers = []

	def __init__(self, urls):
		self.monitors = [Monitor(url) for url in urls]

	def one(self):
		responses = [(m.url, m.ping()) for m in self.monitors]

		for response in responses:
			for observer in self.observers:
				observer(*response)

	def run(self):
		while True:
			self.one()
			sleep(10)


#
# basic observers
#

def all_printer(url, response):
	print url, response.response_code


def air_horn(url, response):
	if response.response_code >= 300:
		print '\n', '*' * 80
		print 'AwOOOOOOGA!!! {0} is down!'.format(url)
		print '\n', '*' * 80


#
# entry point
#

def main():
	hub = Hub(urls)
	hub.observers.append(all_printer)
	hub.observers.append(air_horn)

	hub.run()


if __name__ == '__main__':
	main()
