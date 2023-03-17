import http.client
import apiKey
import listSchedules

conn = http.client.HTTPSConnection("api.pagerduty.com")

objSchedules = listSchedules

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={apiKey.getApiKey('../NoGithub.txt')}"
    }

conn.request("DELETE", "/schedules/P8C454S", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))