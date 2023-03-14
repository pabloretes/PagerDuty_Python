
import requests

QUERY = ''

def list_schedules(API_KEY):
    url = 'https://api.pagerduty.com/schedules'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'query': QUERY
    }
    r = requests.get(url, headers=headers, params=payload)
    print(r.json())

if __name__ == '__main__':
    list_schedules()
