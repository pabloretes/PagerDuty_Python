import requests

payload = {
        'query': ''
}

url = 'https://api.pagerduty.com/services'

def getServices(ApiKey):
    headers = {

        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
    }

    r = requests.get(url, headers=headers, params=payload)
    jsonObj = r.json()
    return (jsonObj)