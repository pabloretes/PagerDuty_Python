import http.client
import json

conn = http.client.HTTPSConnection("api.pagerduty.com")

payload ={
  "relationships": [
    {
      "supporting_service": {
        "id": "PUB6WGJ",
        "type": "technical_service_reference"
      },
      "dependent_service": {
        "id": "PKUULRK",
        "type": "business_service_reference"
      },
      "id": "DQVP7E6G0E8AC3NR",
      "type": "service_dependency"
    }
  ]
}
headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': "Token token=u+M1ooHmsW2rTsW7saCg"
    }

conn.request("POST", "/service_dependencies/associate", json.dumps(payload), headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))