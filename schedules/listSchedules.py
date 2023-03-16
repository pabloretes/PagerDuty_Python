import http.client

import apiKey

api_key = apiKey.getApiKey()

conn = http.client.HTTPSConnection("api.pagerduty.com")

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': "Token token=u+M1ooHmsW2rTsW7saCg"
    }

conn.request("GET", "/schedules", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))