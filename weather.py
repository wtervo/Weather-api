import configparser
import requests
import sys
from weatherprint import w_print
 
def api_key():
	"""
	Get the OpenWeatherMap.com api key from the .ini file
	"""
	
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['OpenWeatherMap']['apikey']
 
def get_weather(api_key, location):
	"""
	Get the weather data of the desired location through the service's api
	"""
	
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
	r = requests.get(url, timeout=3)
	return r.json()
 
def main():
	"""
	Display weather data for every city given as an argument in the command line
	"""
	
	#number of system arguments
	arg_n = len(sys.argv)
	if (arg_n < 2) or (arg_n > 5):
		exit("You need to give 1 to 4 Finnish cities as argument(s).")
	else:
		api = api_key()
		for i in range(1, arg_n):
			#add "fi" to make sure a correct city is chosen
			location = sys.argv[i] + ",fi"

			weather = get_weather(api, location)
			
			#for false city names, display an error message and then move to the next argument
			try:
				w_print(weather)
			except KeyError:
				print("ERROR: \"{}\" is most likely not a valid city name. Remember to separate the commas with empty spaces, ie. \"x, y, z\".\n".format(sys.argv[i].strip(",")))
 
if __name__ == '__main__':
	main()