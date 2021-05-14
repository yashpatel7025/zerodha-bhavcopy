from django.shortcuts import render
from django.core.cache import cache
from zerodha import settings
from django.utils import timezone

import csv, redis, json
import sys
import random
import requests
import zipfile
from io import BytesIO
import os
import datetime
from .utils import *

def convert_csv_to_list(csv_file):
    with open(csv_file, encoding='utf-8') as csvf:
        csv_data = csv.reader(csvf)
        data=[]
        for row in csv_data:
            dictn={
    		"code": row[0],
    		"name": row[1].strip(),
    		"open": row[4],
    		"high": row[5],
    		"low": row[6],
    		"close": row[7] } 
            data.append(dictn)
        return data


def get_redis_data(csv_file, name):
	cache_name = csv_file
	if(cache_name in cache):
		data = cache.get(cache_name)
		data= list(filter(lambda m: True if m["name"].lower().startswith(name) else False, data))
		return data
	return None

def save_data_to_redis(cache_name, data):
	cache.set(cache_name, data, timeout=settings.DEFAULT_TIMEOUT)

def get_data(name):
	for minus_days in [0, -1, -2, -3]:
		date = get_localtime() + datetime.timedelta(days=minus_days)
		date_str = str((get_localtime() + datetime.timedelta(days=minus_days)).date())
		zip_url = "https://www.bseindia.com/download/BhavCopy/Equity/" + "EQ" + date_str[8:10] + date_str[5:7] + date_str[2:4] + "_CSV.ZIP"
		csv_file = "./zips/" + "EQ" + date_str[8:10] + date_str[5:7] + date_str[2:4] + ".CSV"
		data = get_redis_data(csv_file, name)
		if data:
			return data, zip_url, date.strftime("%d %b %Y")
	return None, "#", "not available"


def download_and_save_data():
	for minus_days in [0, -1, -2, -3]:
		date = get_localtime() + datetime.timedelta(days=minus_days)
		date_str = str((get_localtime() + datetime.timedelta(days=minus_days)).date())
		zip_url = "https://www.bseindia.com/download/BhavCopy/Equity/" + "EQ" + date_str[8:10] + date_str[5:7] + date_str[2:4] + "_CSV.ZIP"
		csv_file = "./zips/" + "EQ" + date_str[8:10] + date_str[5:7] + date_str[2:4] + ".CSV"

		header = {
			    'Accept-Encoding': 'gzip, deflate, sdch, br',
			    'Accept-Language': 'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
			    'Host': 'www.bseindia.com',
			    'Referer': 'https://www.bseindia.com/',
			    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
				'X-Requested-With': 'XMLHttpRequest'
		}
		response = requests.get(zip_url,headers=header, stream=True)
		if response.status_code == 200:
			files = zipfile.ZipFile(BytesIO(response.content))
			files.extractall("./zips/")
			data_to_save = convert_csv_to_list(csv_file)
			save_data_to_redis(csv_file, data_to_save)
			return

def get_bhavcopy(request):
	name= request.GET.get("name")
	if not name:
		name="reliance"

	data, zip_url, date = get_data(name.lower())

	context={
	"data" : data if data else [],
	"zip_url" : zip_url,
	"date" : date
	}

	return render(request, 'bhavcopy.html', context=context)


