import datetime
import logging as log
from setuptools._vendor.pyparsing import basestring

from .models import DjLogAdmin

def set_error_to_log(request, content):
	try:
		now = datetime.datetime.now()
		device_id = request.device.device_id

		log = DjLogAdmin(date=now, device_id=device_id,
						content=content)
	except Exception:
		log = DjLogAdmin(date=now, content=content)

	log.save()


def get_data_log(filter, value):
	try:
		if isinstance(filter, basestring):
			if filter.lower().strip() == "date":
				log = DjLogAdmin.objects.filter(date=value)
			elif filter.lower().strip() == 'username':
				log = DjLogAdmin.objects.filter(device_id=value)
			else:
				return None
		else:
			return None
		return log
	except Exception:
		return None