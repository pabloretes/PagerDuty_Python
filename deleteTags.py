import http.client

import apiKey
import listTags
import tags

objTags = listTags.getTags()
conn = http.client.HTTPSConnection("api.pagerduty.com")
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={apiKey.getApiKey()}"
    }

for tag in objTags['tags']:
    conn.request("DELETE", f"/tags/{tag['id']}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))