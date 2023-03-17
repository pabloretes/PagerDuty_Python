import requests
import json
import http.client


def create_escalation_policy(ApiKey):
    payload = {
      "escalation_policy": {
        "type": "escalation_policy",
        "name": "Acme Hotel Escalation Policy",
        "escalation_rules": [
          {
            "escalation_delay_in_minutes": 30,
            "targets": [
              {
                "id": "PEYSGVF",
                "type": "user_reference"
              }
            ]
          }
        ],
        "services": [
          {
            "id": "PIJ90N7",
            "type": "service_reference"
          }
        ],
        "num_loops": 2,
        "on_call_handoff_notifications": "if_has_services",
        "teams": [
          {
            "id": "PQ9K7I8",
            "type": "team_reference"
          }
        ],
        "description": "Here is the ep for the engineering team."
      }
    }


    conn = http.client.HTTPSConnection("api.pagerduty.com")

    payload2 = "{\n  \"escalation_policy\": {\n    \"type\": \"escalation_policy\",\n    \"name\": \"Engineering Escalation Policy\",\n    \"escalation_rules\": [\n      {\n        \"escalation_delay_in_minutes\": 30,\n        \"targets\": [\n          {\n            \"id\": \"PEYSGVF\",\n            \"type\": \"user_reference\"\n          }\n        ]\n      }\n    ],\n    \"services\": [\n      {\n        \"id\": \"PIJ90N7\",\n        \"type\": \"service_reference\"\n      }\n    ],\n    \"num_loops\": 2,\n    \"on_call_handoff_notifications\": \"if_has_services\",\n    \"teams\": [\n      {\n        \"id\": \"PQ9K7I8\",\n        \"type\": \"team_reference\"\n      }\n    ],\n    \"description\": \"Here is the ep for the engineering team.\"\n  }\n}"

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'From': "",
        'Authorization': "Token token=u+M1ooHmsW2rTsW7saCg"
        }

    conn.request("POST", "/escalation_policies", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))