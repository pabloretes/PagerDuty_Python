import requests

def add_user_to_team(API_KEY, TEAM_ID, USER_ID):
    url = 'https://api.pagerduty.com/teams/{tid}/users/{uid}'.format(
        tid=TEAM_ID,
        uid=USER_ID
    )
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json'
    }

    try:
        r = requests.put(url, headers=headers)
        print(' Code: {code}'.format(code=r.status_code),'asignando a Team...',TEAM_ID)
    except requests.exceptions.HTTPError as err:
        print('Something went wrong. Code: {code}'.format(code=r.status_code),r.reason)

if __name__ == '__main__':
    add_user_to_team()
