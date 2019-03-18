# -*- coding: utf-8 -*-

import datetime
import pytz

def utc_to_local(utc_time):
	"""
	Transforms UTC timestrings to local (Finnish) time
	"""
	
	d = datetime.datetime.utcfromtimestamp(utc_time)#.strftime('%d/%m/%Y %H:%M:%S')
	d = pytz.UTC.localize(d)
	pst = pytz.timezone('Europe/Helsinki')
	d = d.astimezone(pst).strftime('%d/%m/%Y %H:%M:%S')
	date, time = d.split(" ")
	return date, time

def w_print(weatherdata):
	"""
	Formats the weather data into more readable form
	"""
	
	date, local_time = utc_to_local(weatherdata["dt"])
	sr_date, sunrise = utc_to_local(weatherdata["sys"]["sunrise"])
	ss_date, sunset = utc_to_local(weatherdata["sys"]["sunset"])
	print("Weather data in {} ({}) on {} at {}:".format(weatherdata["name"], weatherdata["sys"]["country"], date, local_time))
	print("Weather description: {} - {}".format(weatherdata["weather"][0]["main"], weatherdata["weather"][0]["description"]).title())
	print("Current temperature: {} \xb0C (Min: {} \xb0C, Max {} \xb0C)".format(weatherdata["main"]["temp"], weatherdata["main"]["temp_min"], weatherdata["main"]["temp_max"]))
	if weatherdata["wind"]:
		print("Wind: {} m/s".format(weatherdata["wind"]["speed"]))
	#check if certain keys are present and plot values accordingly
	if "rain" in weatherdata:
		if "3h" and "1h" in weatherdata["rain"]:
			print("Rain: {} mm in the last hour, {} in the last 3 hours".format(weatherdata["rain"]["1h"], weatherdata["rain"]["3h"]))
		elif "3h" in weatherdata["rain"]:
			print("Rain: {} mm in the last 3 hours".format(weatherdata["rain"]["3h"]))
		else:
			print("Rain: {} mm in the last hour".format(weatherdata["rain"]["1h"]))
	if "snow" in weatherdata:
		if "3h" and "1h" in weatherdata["snow"]:
			print("Snow: {} mm in the last hour, {} in the last 3 hours".format(weatherdata["snow"]["1h"], weatherdata["snow"]["3h"]))
		elif "3h" in weatherdata["snow"]:
			print("Snow: {} mm in the last 3 hours".format(weatherdata["snow"]["3h"]))
		else:
			print("Snow: {} mm in the last hour".format(weatherdata["snow"]["1h"]))
	if "clouds" in weatherdata:
		print("Cloud percentage: {} %".format(weatherdata["clouds"]["all"]))
	print("Humidity percentage: {} %".format(weatherdata["main"]["humidity"]))
	print("Air pressure: {} hPa = {} bar".format(weatherdata["main"]["pressure"], int(weatherdata["main"]["pressure"])/1000))
	print("Visibility: {} km".format(int(weatherdata["visibility"])/1000))
	print("Time of sunrise on {}: {}".format(sr_date, sunrise))
	#newline symbol for the last printable value to make multiple data prints clearer
	print("Time of sunset on {}: {}\n".format(ss_date, sunset))