import requests
import json
import csv
from escalationPolicies import findEscalationPolicy

url = 'https://api.pagerduty.com/services'


def create_service(ApiKey):
    with open("services/servicesList.csv", newline='') as csvServices:
        nameEscalationPolicy = "Acme Hotel Escalation Policy"
        idEscalationPolicy = findEscalationPolicy.findEscalationPolicyByName(ApiKey,nameEscalationPolicy)

        fileReader = csv.reader(csvServices)
        for userData in fileReader:
            headers = {
                'Content-Type': "application/json",
                'Accept': "application/vnd.pagerduty+json;version=2",
                'Authorization': f"Token token={ApiKey}"
            }

            NAME = userData[1]
            DESCRIPTION = 'This service Supports Hotel Operation'
            ESCALATION_POLICY_ID = idEscalationPolicy
            TYPE = 'service'
            AUTO_RESOLVE_TIMEOUT = 14400  # 4 hours
            ACKNOWLEDGEMENT_TIMEOUT = 1800  # 30 minutes
            TEAMS = []
            INCIDENT_URGENCY = 'high'  # used during support hours or as default urgency
            OUTSIDE_SUPPORT_HOURS_URGENCY = 'low'
            SCHEDULED_ACTIONS = []
            SUPPORT_HOURS = {
                'type': 'fixed_time_per_day',
                'time_zone': 'UTC',
                'days_of_week': [1, 2, 3, 4, 5],
                'start_time': '09:00:00',
                'end_time': '17:00:00'
            }
            INTEGRATIONS = []
            ADDONS = []

            payload = {
                'service': {
                    'name': NAME,
                    'description': DESCRIPTION,
                    'escalation_policy': {
                        'id': ESCALATION_POLICY_ID,
                        'type': 'escalation_policy'
                    },
                    'type': TYPE,
                    'auto_resolve_timeout': AUTO_RESOLVE_TIMEOUT,
                    'acknowledgement_timeout': ACKNOWLEDGEMENT_TIMEOUT,
                    'teams': TEAMS,
                    'scheduled_actions': SCHEDULED_ACTIONS,
                    'integrations': INTEGRATIONS,
                    'addons': ADDONS,
                    'support_hours': SUPPORT_HOURS
                }
            }

            if not SUPPORT_HOURS:
                payload['service']['incident_urgency_rule'] = {
                    'type': 'constant',
                    'urgency': INCIDENT_URGENCY
                }
            else:
                payload['service']['incident_urgency_rule'] = {
                    'type': 'use_support_hours',
                    'during_support_hours': {
                        'type': 'constant',
                        'urgency': INCIDENT_URGENCY
                    },
                    'outside_support_hours': {
                        'type': 'constant',
                        'urgency': OUTSIDE_SUPPORT_HOURS_URGENCY
                    }
                }

            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                r.raise_for_status()
                jsonObj = r.json()
                print(' Code: {code},'.format(code=r.status_code), 'Creating Service...')
                      #jsonObj['service']['id'],jsonObj['service']['name'])
            except requests.exceptions.HTTPError as err:
                print(' Something went wrong. Code: {code}'.format(code=r.status_code), r.reason,
                      jsonObj['service']['id'], jsonObj['service']['name'])

if __name__ == '__main__':
    create_service()

