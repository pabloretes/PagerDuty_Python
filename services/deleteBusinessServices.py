import http.client
import requests

def delete_business_services(ApiKey, listServices):

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
    }

    for service in listServices['business_services']:
        url = 'https://api.pagerduty.com/business_services/{id}'.format(id=service['id'])

        try:
            r = requests.delete(url, headers=headers)
            r.raise_for_status()
            print('Code: {code}, deleting business service... '.format(code=r.status_code), service['id'])

        except requests.exceptions.HTTPError as err:
            print('Something went wrong. Code: {code}'.format(code=r.status_code), r.reason, service['id'])