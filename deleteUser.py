import requests


def delete_user(API_KEY, userId, name):
    ID = userId
    url = 'https://api.pagerduty.com/users/{id}'.format(id=ID)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }

    try:
        r = requests.delete(url, headers=headers)
        r.raise_for_status()
        print('Code: {code}, deleting User... '.format(code=r.status_code), userId, name)
    except requests.exceptions.HTTPError as err:
        print('Something went wrong. Code: {code}'.format(code=r.status_code), r.reason, userId)

    return ID

    if __name__ == '__main__':
        delete_user()
