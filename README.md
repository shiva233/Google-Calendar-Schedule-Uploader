# Google Calendar Schedule Uploader

Time blocking is a very important skill to me, it has helped me be incredibly productive over the summer and I don't know what I would do without it. However using Google Calendar to timeblock has always been a bit tedious for me, with the need to add each event individually and color-code them, and then when there is a disruption having to manually move everything down or up etc. To streamline this process, I developed a script that speeds up uploading a timeblocked day to Google Calendar. This project helped me learn and demonstrate the integration of the Google Calendar API with Python and the basics of authentication.

PS. This is my first time writing a ReadME for a project, so I apologize if any instructions are unclear.

## Features

- **Google Calendar Integration**: Uploads custom schedules to Google Calendar.
- **Event Creation**: Creates events with specified start and end times, summary, and color ID.
- **Automatic Authentication**: Handles authentication using OAuth 2.0 and stores tokens.


## Pre-Usage Setup

### 1. **Install Requirements**

   Install the required Python libraries using pip:

   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

### 2. Obtain Google API Credentials

- Go to the Google Cloud Console.
- Create a new project.
- Enable the Google Calendar API for your project.
- Create credentials (OAuth 2.0 Client IDs) and download the credentials.json file. (you might need to rename the file to credentials.json if it is not already)
- Put this credentials.json in the same folder as the Python script

### 3. Authentication
- Before adding your schedule run the Python file
- Authorize access to your Google account
- If it says access denied go back to your Google Cloud Console and add your email as a test user

## Usage

### 1. Modify the base_date
Modify the base_date in the main() function to correspond with the date you would like to add events for in YEAR/MONTH/DAY
#### Example
Here's an example
```python
#Saturday Schedule
base_date = datetime.date(2024, 7, 20)
```

### 2. Modify the Schedule

  

  Edit the schedule list in the main() function of calendar_upload.py to include your desired events. Each event is defined by a tuple containing:

- Event summary (this is the name of the event)
- Start hour
- Start minute
- End hour
- End minute
- Color ID (Google Calendar color ID, CHART LINKED BELOW)
- ![image](https://github.com/user-attachments/assets/5db1c5bd-8b2c-4d83-a71b-b3cb30995b05)

  #### Example
  Here's an example of a schedule entry:
  ```python
  ("Wake up Morning routine", 9, 0, 9, 30, '5')
  ```
  This entry will create an event titled "Wake up Morning routine" from 9:00 AM to 9:30 AM with color ID '5'.

### 3. Run the Script

Execute the script to upload the schedule to your Google Calendar and enjoy!

## Notes
- The script assumes the time zone is 'America/Toronto'. Adjust the time zone in the create_event() function if needed.
- Events that end before they start are considered as spanning to the next day.
- Currently, it has issues with events that go more than one day for example 9pm - 1am (next day)
- This example schedule was with time blocking in mind which is why the program is configured to only make events for one day at a time

## Future Plans:

I plan to significantly expand the capabilities of the Google Calendar Schedule Uploader by integrating the ChatGPT API. This enhancement will allow the tool to intelligently adjust schedules in response to disruptions, providing a more flexible and adaptive time management solution.

The integration will work as follows:

- Intelligent Rescheduling: The user will be able to type in disruptions they have for a certain day into the terminal (e.g., "I woke up at 11am instead of 9am, please adjust my Monday schedule accordingly"). The ChatGPT API will then analyze their base schedule and make modifications to account for the disruption. The adjusted schedule will be automatically uploaded to Google Calendar.

- Handling Various Disruptions: The system will handle various types of disruptions such as unexpected tasks, meeting overruns, and personal commitments, ensuring that users can maintain an organized and effective schedule despite changes.

- User Interaction: Users will interact with the new features through a terminal interface where they can input disruptions along with their base schedule. The tool will then process this information and provide an updated schedule.

- Time saving: Reduces the need for manual adjustments, saving users valuable time keeps them productive. Ensures that users' schedules remain flexible and adaptive to changes.


By adding these features im going to hopefully make a robust tool that I can use for myself and hopefully for others to make time blocking more streamlined and efficient

## License
This project is licensed under the MIT License




