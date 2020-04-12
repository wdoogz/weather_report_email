# weather_report_email

This is a program that allows you to send emails with weather updates. to one or more users for one or more cities.

usage for bare command line use.

arguments are:

-c you must create a file with city codes from openweathermap.org and place separate them by new line

-w a path to a random file, it should not exist already.

-r path to a file with the email addresses you wish to send to separated by new line

-sec path to file with email address and password - email on first line password on second

-a apikey from oopenweathermap.org (its free)

__init__.py -c [path to cities file] -w [path to weather file] -r [recipient file] -sec [path to credentials] -a [api key]
