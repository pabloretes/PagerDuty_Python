import requests
import json

import findTeam
import findUser
from services import findServices
from schedules import findSchedule



def create_escalation_policy(ApiKey):
    idUser = findUser.findUserbyName(ApiKey, 'Responder21')
    idSchedule = findSchedule.findSchedulebyName(ApiKey,'Acme Hotel Support Center Rotation')
    idTeam = findTeam.findTeambyName(ApiKey,'Central Engineering and Operations')

    summary = "Acme Hotel Escalation Policy"
    name = "Acme Hotel Escalation Policy"

    payload = {
      "escalation_policy": {
        "type": "escalation_policy",
        "summary": summary,
        "name": name,
        "escalation_rules": [
          {
            "escalation_delay_in_minutes": 30,
            "targets": [
              {
                "id": idUser,
                "type": "user_reference",
              },
              {
                "id": idSchedule,
                "type": "schedule_reference",
              }
            ]
          }
        ],

        "num_loops": 2,
        "teams": [
          {
            "id": idTeam,
            "type": "team_reference",
          }
        ]
      }
    }

    url = 'https://api.pagerduty.com/escalation_policies'

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'From': "",
        'Authorization': "Token token=u+M1ooHmsW2rTsW7saCg"
        }

    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r.raise_for_status()
        jsonObj = r.json()
        print(' Code: {code},'.format(code=r.status_code), 'Creating Escalation Policy...',
              jsonObj['escalation_policy']['id'], jsonObj["escalation_policy"]["summary"])
    except requests.exceptions.HTTPError as err:
        print(' Something went wrong. Code: {code} Escalation Policy'.format(code=r.status_code), r.reason)
