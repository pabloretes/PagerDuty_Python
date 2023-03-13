import requests


def delete_user(API_KEY, userId):
    ID = userId
    url = 'https://api.pagerduty.com/users/{id}'.format(id=ID)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }

    r = requests.delete(url, headers=headers)
    return ID


if __name__ == '__main__':
    delete_user()
