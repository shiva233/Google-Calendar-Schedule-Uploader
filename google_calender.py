import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(service, start_time, end_time, summary, colorId):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'America/Toronto',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'America/Toronto',
        },
        'colorId': colorId
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

def main():
    service = authenticate_google_calendar()

    # Saturday Schedule
    base_date = datetime.date(2024, 7, 20)  # Example date for Saturday

    schedule = [
        ("Wake up Morning routine", 9, 0, 9, 30, '5'),
        ("Shower", 9, 30, 10, 0, '5'),
        ("Free time", 10, 0, 11, 0, '9'),
        ("Breakfast", 11, 0, 11, 30, '5'),
        ("Physics coursework - 2 Pomo", 11, 30, 12, 30, '11'),
        ("Chemistry coursework - 2 Pomo", 12, 30, 13, 30, '10'),
        ("Lunch", 13, 30, 14, 0, '5'),
        ("Math coursework - 2 Pomo", 14, 0, 15, 0, '7'),
        ("Free Time", 15, 0, 15, 30, '9'),
        ("Github Grind - 1 Pomo", 15, 30, 16, 30, '3'),
        ("Catch-up Block", 16, 30, 17, 0, '5'),
        ("Arduino/Side projects/Networking", 17, 0, 18, 0, '1'),
        ("Dinner", 18, 0, 19, 0, '5'),
        ("Work", 19, 0, 23, 0, '1'),
        ("Free time/Relaxation", 23, 0, 0, 0, '9'),
    ]

    for task in schedule:
        summary = task[0]
        start_hour = task[1]
        start_minute = task[2]
        end_hour = task[3]
        end_minute = task[4]
        colorId = task[5]

        # Correctly handle events that cross to the next day
        start_time = datetime.datetime(base_date.year, base_date.month, base_date.day, start_hour, start_minute)
        end_time = datetime.datetime(base_date.year, base_date.month, base_date.day, end_hour, end_minute)
        if end_time <= start_time:
                end_time += datetime.timedelta(days=1)

        create_event(service, start_time, end_time, summary, colorId)

if __name__ == '__main__':
    main()