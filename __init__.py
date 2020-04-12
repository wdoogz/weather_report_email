#!/usr/bin/python3
from weatherby import weather_printer as wp
import send_mail as sm
import itertools
import os
import argparse

args = argparse.ArgumentParser(description="Use the following", usage="""
-c      --citiesfile         Use the path to a cities file, containing city codes from openweathermap api
-w      --weatherfile        Use the path to where you wish to send the weather output.
-r      --recipientfile      Use the path to a list of recipients you want to send this too, separated by new line.
-sec    --credentialfile     Use the path to a file containing your username and password to the email account you wish to use on different lines
-a      --apikey             Use your own apikey for openweatherapi
""")
args.add_argument("-c", "--citiesfile", action='store', type=str, required=True)
args.add_argument("-w", "--weatherfile", action='store', type=str, required=True)
args.add_argument("-r", "--recipientfile", action='store', type=str, required=True)
args.add_argument("-sec", "--credentialfile", action='store', type=str, required=True)
args.add_argument("-a", "--apikey", action='store', required=False)
args = args.parse_args()

URL = "http://api.openweathermap.org/data/2.5/forecast?id=\
{}&APPID={}"
CITIES = open(args.citiesfile, "r").read().split()
WEATHER_FILE = args.weatherfile
RECIPIENT_FILE = args.recipientfile
SEND_EMAIL_CREDS = args.credentialfile

def weather_report_mail(cities, url, weather_file, recipient_file, send_email_creds, apikey):
    rfs = []
    with open(weather_file, 'a') as file_to_write:
        for city in cities:
            select_city = str("\n\n" + wp(city, url, apikey)[0] + "\n")
            file_to_write.write(select_city)

            for (x, y) in zip(wp(city, url, apikey)[1], wp(city, url, apikey)[2]):
                y = round(((y - 273.15)*1.8)+32, 2)
                time_temp = ' '.join([str(x) + "    " + str(y), "F \n"])
                file_to_write.write(time_temp)
    
    with open(recipient_file, "r") as rf:
        for line in rf:
            rfs.append(line.strip())
    for recp in rfs:
        sm.send_email(sm.login(send_email_creds), recp, weather_file)

if not os.path.isfile(WEATHER_FILE):
    weather_report_mail(CITIES, URL, WEATHER_FILE, RECIPIENT_FILE, SEND_EMAIL_CREDS, args.apikey)
else:
    os.remove(WEATHER_FILE)
    weather_report_mail(CITIES, URL, WEATHER_FILE, RECIPIENT_FILE, SEND_EMAIL_CREDS, args.apikey)
