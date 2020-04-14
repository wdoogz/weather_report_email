#!/usr/bin/python3
import requests
import json

def weather_printer(city, url, apikey):
    get_weather = requests.get(url.format(city, apikey)).json()
    print(get_weather)
    cityname = get_weather['city']['name']
    templist = []
    timelist = []
    for v in get_weather['list']:
      templist.append(v['dt_txt'])
      timelist.append(v['main']['temp'])
    return cityname, templist, timelist
