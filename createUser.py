import json
import csv
import requests

import addUsertoteam
import findTeam

from_email = "sinclairchuli@proton.me"
pagerduty_team_id = ""
userObjects = []
idTeam = ""

def create_user(API_KEY):
    url = 'https://api.pagerduty.com/users'
    with open("userslist.csv", newline='') as csvUsers:
        fileReader = csv.reader(csvUsers)
        for userData in fileReader:
            headers = {
                'Content-Type': "application/json",
                'Accept': "application/vnd.pagerduty+json;version=2",
                'From': from_email,
                'Authorization': f'Token token={API_KEY}'
            }

            payload = {
                'user': {
                    'type': 'user',
                    'name': userData[0],
                    'email': userData[1]
                }
            }

            team = userData[3]
            idTeam = findTeam.findTeambyName(team)

            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                jsonUser = r.json()
                idUser = jsonUser['user']['id']
                print('Code: {code},'.format(code=r.status_code), 'Creating User...', idUser,userData[0] )
            except requests.exceptions.HTTPError as err:
                print('Something went wrong. Code: {code}'.format(code=r.status_code),r.reason,userData[0])

            ######################################################
            # To add new user to team
            ######################################################
            addUsertoteam.add_user_to_team(API_KEY,idTeam,idUser)



        if __name__ == '__main__':
            create_user()