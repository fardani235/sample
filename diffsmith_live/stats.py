import logging

log = logging.getLogger(__name__)


def average(items):
	total = sum(item["amount"] for item in items)
	return total / len(items) if items else 0


def fetch(session, url):
	response = session.get(url, timeout=10)
	response.raise_for_status()
	return response.json()


def retry(call, attempts):
	while attempts > 0:
		log.warning("retrying")
		call()
	return None
