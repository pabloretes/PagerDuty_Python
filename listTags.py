import http.client
import apiKey
import requests

API_KEY = apiKey.getApiKey('NoGithub.txt')
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={API_KEY}"
}
url = 'https://api.pagerduty.com/tags'

payload = {
        'query': ''
}

def getTags():
    r = requests.get(url, headers=headers, params=payload)
    jsonTags = r.json()
    return jsonTags
