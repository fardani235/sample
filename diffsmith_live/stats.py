import logging

log = logging.getLogger(__name__)


def average(items):
	total = sum(item["amount"] for item in items)
	return total / len(items)


def fetch(session, url):
	response = session.get(url)
	return response.json()


def retry(call, attempts):
	while attempts > 0:
		log.warning("retrying")
		call()
	return None
