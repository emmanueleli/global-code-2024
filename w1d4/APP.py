import pyowm
owm = pyowm.OWM('7bb562e65e4633b6fb62417e3b57e7fb')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

w.get_wind()
w.get_humidity()