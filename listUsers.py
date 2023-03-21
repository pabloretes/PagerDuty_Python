import requests
import csv

QUERY = ''
TEAM_IDS = []
INCLUDE = []

def list_users(ApiKey):
    url = 'https://api.pagerduty.com/users'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=ApiKey)
    }
    payload = {
        'query': QUERY,
        'team_ids[]': TEAM_IDS,
        'include[]': INCLUDE
    }
    r = requests.get(url, headers=headers, params=payload)
    userDiccionario = r.json()
    return userDiccionario


if __name__ == '__main__':
    list_users()
