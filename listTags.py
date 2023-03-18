import http.client
import apiKey
import requests


url = 'https://api.pagerduty.com/tags'

payload = {
        'query': ''
}

def getTags(API_KEY):
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={API_KEY}"
    }

    r = requests.get(url, headers=headers, params=payload)
    jsonTags = r.json()
    return jsonTags
