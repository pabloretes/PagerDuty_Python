import requests

def delete_team(API_KEY, teamId):

        ID = teamId
        url = 'https://api.pagerduty.com/teams/{id}'.format(id=ID)
        headers = {
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Authorization': 'Token token={token}'.format(token=API_KEY)
        }

        r = requests.delete(url, headers=headers)
        return ID

if __name__ == '__main__':
    delete_team()
