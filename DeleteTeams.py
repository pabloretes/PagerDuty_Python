import http.client
import json
import requests

API_KEY = 'u+M1ooHmsW2rTsW7saCg'
teamObjects = []

conn = http.client.HTTPSConnection("api.pagerduty.com")
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': f"Token token={API_KEY}"
}

conn.request("GET", "/teams", headers=headers)

# Obtengo coleccion de Teams
res = conn.getresponse()
data = res.read()
teamObjects = data.decode("utf-8")
teamDiccionario = json.loads(data)

for team in teamDiccionario["teams"]:
    ID = team["id"]

    def delete_team():
        url = 'https://api.pagerduty.com/teams/{id}'.format(id=ID)
        headers = {
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Authorization': 'Token token={token}'.format(token=API_KEY)
        }
        r = requests.delete(url, headers=headers)
        print('Status Code: {code}'.format(code=r.status_code))
        print(r.text)


    if __name__ == '__main__':
        delete_team()
