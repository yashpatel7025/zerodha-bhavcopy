from celery import shared_task
from .views import download_and_save_data

@shared_task
def download_bhavcopy_at_6pm_everyday():
	download_and_save_data()
	print("done")
	