import json
import datetime 
from datetime import date

thisYear = int(date.today().year)
thisMonth = int(date.today().month)
thisDay = int(date.today().day)
todayDate = datetime.datetime(thisYear, thisMonth, thisDay)

# ---------------------------------------------
file = open("Response.json", "r")
output = open(r"Upcoming.txt", "w")

dataResponse = json.load(file)

print("Upcoming Holidays are:")

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