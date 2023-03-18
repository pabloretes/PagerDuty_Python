import requests
def delete_escalation_policies(ApiKey, listObjects):

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
        }

    for obj in listObjects['escalation_policies']:
        url = 'https://api.pagerduty.com/escalation_policies/{id}'.format(id=obj['id'])

        try:
            r = requests.delete(url, headers=headers)
            r.raise_for_status()
            print('Code: {code}, deleting Escalation Policy... '.format(code=r.status_code), obj['id'],obj['name'])

        except requests.exceptions.HTTPError as err:
            print('Something went wrong. Code: {code} Escalation Policy'.format(code=r.status_code), r.reason, obj['id'])

