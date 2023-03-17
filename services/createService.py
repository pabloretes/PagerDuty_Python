import requests
import json

# my chosen parameters
NAME = 'ACME Hotel Payment Processing'
DESCRIPTION = 'This service support all payments processed through the web'
ESCALATION_POLICY_ID = 'P1JZCPN'
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

def create_service(ApiKey):
    url = 'https://api.pagerduty.com/services'
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={ApiKey}"
    }

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

    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())


if __name__ == '__main__':
    create_service()

