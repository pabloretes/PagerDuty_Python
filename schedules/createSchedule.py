import requests
import apiKey
import json
import findUser

def create_shedule(ApiKey):
    idResponder21 = findUser.findUserbyName(ApiKey, 'Responder21')
    idResponder22 = findUser.findUserbyName(ApiKey, 'Responder22')

    payload = {
      "schedule": {
        "name": "Acme Hotel Support Center Rotation",
        "type": "schedule",
        "time_zone": "America/New_York",
        "description": "Acme Hotel Support T1 24x7",
        "schedule_layers": [
          {
            "name": "Night Shift",
            "start": "2015-11-06T20:00:00-08:00",
            "rotation_virtual_start": "2015-11-06T20:00:00-08:00",
            "rotation_turn_length_seconds": 86400,
            "users": [
              {
                "user": {
                  "id": idResponder21,
                  "type": "user_reference"
                }
              }
            ],
            "restrictions": [
              {
                "type": "daily_restriction",
                "start_time_of_day": "08:00:00",
                "duration_seconds": 43200
              }
            ]
          },
    {
            "name": "Day Shift",
            "start": "2015-11-06T08:00:00-20:00",
            "rotation_virtual_start": "2015-11-06T08:00:00-20:00",
            "rotation_turn_length_seconds": 86400,
            "users": [
              {
                "user": {
                  "id": idResponder22,
                  "type": "user_reference"
                }
              }
            ],
            "restrictions": [
              {
                "type": "daily_restriction",
                "start_time_of_day": "20:00:00",
                "duration_seconds": 43200
              }
            ]
          }
        ]
      }
    }

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
        }

    url = 'https://api.pagerduty.com/schedules'

    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r.raise_for_status()
        jsonTag = r.json()
        print(' Code: {code},'.format(code=r.status_code), 'Creating & Adding Schedule...')
    except requests.exceptions.HTTPError as err:
        print(' Something went wrong. Code: {code}'.format(code=r.status_code),r.reason)

