import requests
import json
import datetime
from datetime import date

CALENDARIFIC_API = "https://calendarific.com/api/v2/holidays"
QUERY_STRING = "?"
API_KEY = "" # API Key goes here
API_KEY_PARAM = f"api_key={API_KEY}"
COUNTRY = "&country=US"
YEAR = "&year=2024"
LOCATION = "&location=Connecticut"
TYPE = "&type=national"

API_URL = f"{CALENDARIFIC_API}{QUERY_STRING}{API_KEY_PARAM}{COUNTRY}{YEAR}{LOCATION}{TYPE}"

thisYear = int(date.today().year)
thisMonth = int(date.today().month)
thisDay = int(date.today().day)

todayDate = datetime.datetime(thisYear, thisMonth, thisDay)

output = open(r"Upcoming.txt", "w")

# ---------------------------------------------
response = requests.get(API_URL)

dataResponse = response.json()

if response.status_code != 200:
    print("Error with API request")
    exit()

for x in dataResponse['response']['holidays']:
    holiday = x['name']
    date = x['date']['iso']
    splitDate = date.split("-")
    
    year = int(splitDate[0])
    month = int(splitDate[1])
    day = int(splitDate[2])
    
    holidayDate = datetime.datetime(year, month, day)

    if holidayDate > todayDate:
        h = f"{holiday:<20} | {date}"
        # print(h)
        output.write(h + "\n")

output.close()