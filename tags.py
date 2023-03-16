import http.client
import apiKey
import json

API_KEY = apiKey.getApiKey()
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={API_KEY}"
}
conn = http.client.HTTPSConnection("api.pagerduty.com")

class tagEntitie:
    def createTag(NAMETAG):
        tags = NAMETAG.split()
        for tag in tags:
            payload = {
                'tag': {
                    'type': 'tag',
                    'label': tag
                }
            }


            conn.request("POST", "/tags", json.dumps(payload), headers)

            res = conn.getresponse()
            data = res.read()

            print(data.decode("utf-8"))
