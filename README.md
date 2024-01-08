# Holiday Upcoming Events Checker

A Python script to fetch upcoming holidays using the Calendarific API.
## Installation

1. Clone the repository:
2. Install the required packages:
   ```bash
   pip install requests

## Usage

1. Obtain your Calendarific API key from Calendarific.
2. Open API_Request.py and replace API_KEY with your actual API key.
3. Run the script:
   python API_Request.py
4. Check the Upcoming.txt file for the list of upcoming holidays.
Using a Local Response File
If you don't have a Calendarific API key, you can use the local.py script along with the included response.json file. Follow these steps:
  1. Run the local.py script:
       python local.py
  2. Check the Upcoming.txt file for the list of upcoming holidays based on the local response. Note: The response.json file contains sample data and can be replaced with a new file obtained from Calendarific or any other source.

