import http.client
import requests
import apiKey

conn = http.client.HTTPSConnection("api.pagerduty.com")

payload = {
        'query': ''
}

url = 'https://api.pagerduty.com/schedules'

def getSchedules(ApiKey):
    headers = {

        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
    }

    conn.request("GET", "/schedules", headers=headers)
    r = requests.get(url, headers=headers, params=payload)
    jsonObj = r.json()
    return(jsonObj)

