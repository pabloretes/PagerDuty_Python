import requests

import apiKey

QUERY = ''
def list_teams():
    url = 'https://api.pagerduty.com/teams'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=apiKey.getApiKey('NoGithub.txt'))
    }
    payload = {
        'query': QUERY
    }
    r = requests.get(url, headers=headers, params=payload)
    jsonTeams = r.json()
    return jsonTeams


if __name__ == '__main__':
    list_teams()