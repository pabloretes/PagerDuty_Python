import http.client
import requests

import apiKey
import listTags

def delete_tags(API_KEY,objTags):
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={apiKey.getApiKey('NoGithub.txt')}"
        }

    for tag in objTags['tags']:
        url = 'https://api.pagerduty.com/tags/{id}'.format(id=tag['id'])

        try:
            r = requests.delete(url, headers=headers)
            r.raise_for_status()
            print('Code: {code}, deleting tag... '.format(code=r.status_code), tag['id'], tag['summary'])

        except requests.exceptions.HTTPError as err:
            print('Something went wrong. Code: {code}'.format(code=r.status_code), r.reason, tag['id'], tag['summary'])

