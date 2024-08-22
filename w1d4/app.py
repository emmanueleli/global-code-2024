
import pyowm

owm = pyowm.OWM('7bb562e65e4633b6fb62417e3b57e7fb')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('London,uk')
#w = observation.get_weather()
w = observation.weather

#w.get_wind()
#w.get_humidity()

print(w.wind())
print(w.humidity)
#print(w.rain)
#print(w.heat_index)


from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID= 7bb562e65e4633b6fb62417e3b57e7fb')
pprint(r.json)