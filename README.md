# Google Calendar Schedule Uploader

This project demonstrates how to use the Google Calendar API to upload a schedule from a Python script. The script authenticates with Google and creates calendar events based on a predefined schedule that the user adds.

## Features

- **Google Calendar Integration**: Uploads custom schedules to Google Calendar.
- **Event Creation**: Creates events with specified start and end times, summary, and color ID.
- **Automatic Authentication**: Handles authentication using OAuth 2.0 and stores tokens.


## Pre-Usage Setup

1. **Install Requirements**

   Install the required Python libraries using pip:

   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. Obtain Google API Credentials

- Go to the Google Cloud Console.
- Create a new project.
- Enable the Google Calendar API for your project.
- Create credentials (OAuth 2.0 Client IDs) and download the credentials.json file. (you might need to rename the file to credentials.json if it is not already)
- Put this credentials.json in the same folder as the Python script

3. Authentication
- Before adding your schedule run the Python file
- Authorize access to your Google account
- If it says access denied go back to your Google Cloud Console and add your email as a test user

## Usage

1. Modify the base_date
Modify the base_date in the main() function to correspond with the date you would like to add events for in YEAR/MONTH/DAY
## Example
Here's an example
```python
#Saturday Schedule
base_date = datetime.date(2024, 7, 20)
```

3. Modify the Schedule

  

  Edit the schedule list in the main() function of calendar_upload.py to include your desired events. Each event is defined by a tuple containing:

- Event summary (this is the name of the event)
- Start hour
- Start minute
- End hour
- End minute
- Color ID (Google Calendar color ID, CHART LINKED BELOW)
- ![image](https://github.com/user-attachments/assets/5db1c5bd-8b2c-4d83-a71b-b3cb30995b05)

  ## Example
  Here's an example of a schedule entry:
  ```python
  ("Wake up Morning routine", 9, 0, 9, 30, '5')
  ```
  This entry will create an event titled "Wake up Morning routine" from 9:00 AM to 9:30 AM with color ID '5'.

2. Run the Script

Execute the script to upload the schedule to your Google Calendar and enjoy!

##Notes
- The script assumes the time zone is 'America/Toronto'. Adjust the time zone in the create_event() function if needed.
- Events that end before they start are considered as spanning to the next day.
- Currently, it has issues with events that go more than one day for example 9pm - 1am (next day)
- This example schedule was with time blocking in mind which is why the program is configured to only make events for one day at a time

##License
This project is licensed under the MIT License




