import http.client
import json
import requests
import apiKey

conn = http.client.HTTPSConnection("api.pagerduty.com")

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={apiKey.getApiKey()}"
}

def addTag(type,idteam,tags):
    listTags = tags.split()
    for tag in listTags:
        payload = {
          "add": [
            {
              "type": "tag",
              "label": tag
            }
          ]
        }
        url = f'https://api.pagerduty.com/{type}/{idteam}/change_tags'

        try:
            r = requests.post(url, headers=headers, data=json.dumps(payload))
            r.raise_for_status()
            jsonTag = r.json()
            print(' Code: {code},'.format(code=r.status_code), 'Creating & Adding Tag...', tag)
        except requests.exceptions.HTTPError as err:
            print(' Something went wrong. Code: {code}'.format(code=r.status_code),r.reason)






