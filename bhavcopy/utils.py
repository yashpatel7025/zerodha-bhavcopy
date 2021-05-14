from django.utils import timezone
from zerodha import settings

class MyException(Exception):
    pass

def get_localtime():
	return timezone.localtime(timezone.now())

