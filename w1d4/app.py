
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


