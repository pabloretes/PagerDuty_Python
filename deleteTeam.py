import requests

def delete_team(API_KEY, teamId, name):

        ID = teamId
        url = 'https://api.pagerduty.com/teams/{id}'.format(id=ID)
        headers = {
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Authorization': 'Token token={token}'.format(token=API_KEY)
        }

        try:
            r = requests.delete(url, headers=headers)
            r.raise_for_status()
            print('Code: {code}, deleting Team... '.format(code=r.status_code), teamId, name)
        except requests.exceptions.HTTPError as err:
            print('Something went wrong. Code: {code}'.format(code=r.status_code), r.reason, teamId, name)



        return ID
if __name__ == '__main__':
    delete_team()
