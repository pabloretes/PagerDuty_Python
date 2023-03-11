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
        print(user)


if __name__ == '__main__':
    list_users()
