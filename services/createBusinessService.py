import requests
import findTeam
import json

team = 'Guest Experience'
idTeam = findTeam.findTeambyName(team)
def create_business_service(ApiKey):

    payload = {
        "business_service": {
        "name": "Hotel Support Center",
        "description": "service for our web & mobile clients",
        "point_of_contact": "Pablo Retes",
        "team": {
          "id": idTeam
        }
      }
    }
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
    }

    url = 'https://api.pagerduty.com/business_services'

    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r.raise_for_status()
        jsonObj = r.json()
        print(' Code: {code},'.format(code=r.status_code), 'Creating Business Service...',jsonObj['business_service']['name'], f'| Team assigned: {team}')
    except requests.exceptions.HTTPError as err:
        print(' Something went wrong. Code: {code} Business Service'.format(code=r.status_code), r.reason)



