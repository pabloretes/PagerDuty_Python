import requests
import findTeam
import json
import csv


def create_business_service(ApiKey):
    with open("services/businessserviceslist.csv", newline='') as csvServices:
        fileReader = csv.reader(csvServices)
        for bsData in fileReader:
            nameBusinessService = bsData[0]
            nameTeam = bsData[1]

            idTeam = findTeam.findTeambyName(ApiKey,nameTeam)

            payload = {
                "business_service": {
                "name": nameBusinessService,
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
                print(' Code: {code},'.format(code=r.status_code), 'Creating Business Service...',jsonObj['business_service']['name'], f'| Team assigned: {idTeam}')
            except requests.exceptions.HTTPError as err:
                print(' Something went wrong. Code: {code} Business Service'.format(code=r.status_code), r.reason)



