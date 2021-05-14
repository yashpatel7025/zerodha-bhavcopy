from celery import shared_task
from .views import download_and_save_data

@shared_task
def yash():
	download_and_save_data()
	print("done")
	