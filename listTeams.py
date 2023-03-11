import requests

# Update to match your API key
API_KEY = 'u+M1ooHmsW2rTsW7saCg'

QUERY = ''


def list_teams():
    url = 'https://api.pagerduty.com/teams'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'query': QUERY
    }
    r = requests.get(url, headers=headers, params=payload)
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())


if __name__ == '__main__':
    list_teams()