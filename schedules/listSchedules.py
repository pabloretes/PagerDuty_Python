import http.client
import requests
import apiKey

conn = http.client.HTTPSConnection("api.pagerduty.com")

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={apiKey.getApiKey('../NoGithub.txt')}"
    }

conn.request("GET", "/schedules", headers=headers)

payload = {
        'query': ''
}

url = 'https://api.pagerduty.com/schedules'

def getSchedules():
    r = requests.get(url, headers=headers, params=payload)
    jsonObj = r.json()
    for schedule in jsonObj['schedules']:
        print(schedule)

getSchedules()