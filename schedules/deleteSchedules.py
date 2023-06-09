import requests

def delete_schedules(ApiKey, listSchedules):

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
        }

    for schedule in listSchedules['schedules']:
        url = 'https://api.pagerduty.com/schedules/{id}'.format(id=schedule['id'])

        try:
            r = requests.delete(url, headers=headers)
            r.raise_for_status()
            print('Code: {code}, deleting schedule... '.format(code=r.status_code), schedule['id'],schedule['name'])

        except requests.exceptions.HTTPError as err:
            print('Something went wrong. Code: {code} schedule'.format(code=r.status_code), r.reason, schedule['id'])



