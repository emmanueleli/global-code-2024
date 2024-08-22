from pprint import pprint
import requests
APIKEY = '7bb562e65e4633b6fb62417e3b57e7fb'
location = input("Enter your location: ")
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APIKEY}')
Respond = r.json()
if response "cod"  == "404"
    print("ok")
else print response
pprint(response)