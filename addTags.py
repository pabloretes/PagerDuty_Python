import http.client
import json

import apiKey

conn = http.client.HTTPSConnection("api.pagerduty.com")

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

        headers = {
            'Content-Type': "application/json",
            'Accept': "application/vnd.pagerduty+json;version=2",
            'Authorization': f"Token token={apiKey.getApiKey()}"
            }

        conn.request("POST", f"/{type}/{idteam}/change_tags", json.dumps(payload), headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))