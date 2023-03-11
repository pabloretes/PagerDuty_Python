import requests
API_KEY = 'u+M1ooHmsW2rTsW7saCg'

# Update to match your IDs
TEAM_ID = 'PYJD990'
USER_ID = ''


def add_user_to_team():
    url = 'https://api.pagerduty.com/teams/{tid}/users/{uid}'.format(
        tid=TEAM_ID,
        uid=USER_ID
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
