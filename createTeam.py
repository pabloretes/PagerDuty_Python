import http.client
import json
import csv
import requests

API_KEY = 'u+M1ooHmsW2rTsW7saCg'
teamObjects = []

with open("teamlist.csv", newline='') as csvTeams:
    fileReader = csv.reader(csvTeams)
    for teamData in fileReader:
        name = teamData[0]
        description = teamData[1]
        teamObject: dict[str, str] = {
            "type": "team",
            "name": name,
            "description": description
        }
        teamObjects.append(json.dumps(teamObject))

        conn = http.client.HTTPSConnection("api.pagerduty.com")
        payload = "{\n  \"team\": {\n    \"type\": \"team\",\n    \"name\": \"" + name + "\",\n    \"description\": \"" + description + "\"\n  }\n}"

        headers = {
            'Content-Type': "application/json",
            'Accept': "application/vnd.pagerduty+json;version=2",
            'Authorization': f"Token token={API_KEY}"
        }

        conn.request("POST", "/teams", payload, headers)

        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
