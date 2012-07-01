from datetime import datetime, timedelta

from pyping.model import Response

import pytest


def test_response_must_have_either_response_or_exception():
	Response(response=True)
	Response(exception=True)

	with pytest.raises(ValueError):
		Response()


def test_response_should_not_accept_both():
	with pytest.raises(ValueError):
		Response(response=True, exception=True)


def test_response_should_record_created_time():
	now = datetime.now()
	delta = timedelta(seconds=1)

	moment_ago = now - delta
	next_moment = now + delta

	response = Response(response=True)

	assert moment_ago < response.created < next_moment
