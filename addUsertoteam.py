import requests
import json

# Update to match your API key
API_KEY = 'u+M1ooHmsW2rTsW7saCg'

# Update to match your chosen parameters
QUERY = ''
TEAM_IDS = []
INCLUDE = []


def list_users():
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'query': QUERY,
        'team_ids[]': TEAM_IDS,
        'include[]': INCLUDE
    }
    r = requests.get(url, headers=headers, params=payload)
    print('Status Code: {code}'.format(code=r.status_code))
    userDiccionario = r.json()

    for user in userDiccionario["users"]:
        uid = user["id"]

        add_user_to_team(tid, uid)


if __name__ == '__main__':
    list_users()


def add_user_to_team(teamId, userId):
    url = 'https://api.pagerduty.com/teams/{tid}/users/{uid}'.format(
        tid=teamId,
        uid=userId
    )
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json'
    }
    r = requests.put(url, headers=headers)
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.text)

if __name__ == '__main__':
    add_user_to_team()
