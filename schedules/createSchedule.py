import requests
import json

# payload = "{\n  \"schedule\": {\n    \"name\": \"Daily Engineering Rotation\",\n    \"type\": \"schedule\",\n    \"time_zone\": \"America/New_York\",\n    \"description\": \"Rotation schedule for engineering\",\n    \"schedule_layers\": [\n      {\n        \"name\": \"Night Shift\",\n        \"start\": \"2015-11-06T20:00:00-05:00\",\n        \"rotation_virtual_start\": \"2015-11-06T20:00:00-05:00\",\n        \"rotation_turn_length_seconds\": 86400,\n        \"users\": [\n          {\n            \"user\": {\n              \"id\": \"PXPGF42\",\n              \"type\": \"user_reference\"\n            }\n          }\n        ],\n        \"restrictions\": [\n          {\n            \"type\": \"daily_restriction\",\n            \"start_time_of_day\": \"08:00:00\",\n            \"duration_seconds\": 32400\n          }\n        ]\n      }\n    ]\n  }\n}"

payload = {
  "schedule": {
    "name": "Acme Hotel Support Center Rotation",
    "type": "schedule",
    "time_zone": "America/New_York",
    "description": "Acme Hotel Support T1 24x7",
    "schedule_layers": [
      {
        "name": "Night Shift",
        "start": "2015-11-06T20:00:00-05:00",
        "rotation_virtual_start": "2015-11-06T20:00:00-05:00",
        "rotation_turn_length_seconds": 86400,
        "users": [
          {
            "user": {
              "id": "P64YDN6",
              "type": "user_reference"
            },
            "user": {
              "id": "P2VNCXG",
              "type": "user_reference"
            }
          }
        ],
        "restrictions": [
          {
            "type": "daily_restriction",
            "start_time_of_day": "08:00:00",
            "duration_seconds": 32400
          }
        ]
      }
    ]
  }
}

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': "Token token=u+M1ooHmsW2rTsW7saCg"
    }

url = 'https://api.pagerduty.com/schedules'

try:
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    r.raise_for_status()
    jsonTag = r.json()
    print(' Code: {code},'.format(code=r.status_code), 'Creating & Adding Schedule...')
except requests.exceptions.HTTPError as err:
    print(' Something went wrong. Code: {code}'.format(code=r.status_code),r.reason)

