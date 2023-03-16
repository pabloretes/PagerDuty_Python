import json
import csv
import requests

import addTags
import tags

teamObjects = []
url = 'https://api.pagerduty.com/teams'
file = 'teamlist.csv'
def create_team(API_KEY):
    with open(file, newline='') as csvTeams:
        fileReader = csv.reader(csvTeams)
        for teamData in fileReader:

            headers = {
                'Accept': 'application/vnd.pagerduty+json;version=2',
                'Authorization': 'Token token={token}'.format(token=API_KEY),
                'Content-type': 'application/json'
            }
            payload = {
                'team': {
                    'type': 'team',
                    'name': teamData[0],
                    'description': teamData[1],
                    'summary': teamData[1]
                }
            }

            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                r.raise_for_status()
                jsonTeam = r.json()
                idTeam = jsonTeam['team']['id']
                print('Code: {code},'.format(code=r.status_code), 'Creating Team...',idTeam,teamData[0])

                #######################################
                # to assign tags a team
                addTags.addTag('teams',idTeam,teamData[2])
                #######################################

            except requests.exceptions.HTTPError as err:
                print('Something went wrong. Code: {code}'.format(code=r.status_code),r.reason,teamData[0])





