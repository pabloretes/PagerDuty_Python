import http.client
import json
import requests


def create_email_integration(API_KEY, idService):
    payload = {
        "integration": {
            "type": "generic_email_inbound_integration",
            "name": "Email",
            "service": {
                "id": idService,
                "type": "service_reference",
                "summary": "My Email-Based Integration",
            },
            "integration_email": "acme-hotel-payment-processing-email.03j8yo76@proton-latam.pagerduty.com"
        }
    }

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f'Token token={API_KEY}'
    }

    url = 'https://api.pagerduty.com/services/{id}/integrations'.format(id=idService)

    try:
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        r.raise_for_status()
        jsonObj = r.json()
        print(' Code: {code},'.format(code=r.status_code), 'Creating & Adding Integration...',
              jsonObj['integration']['id'],
              jsonObj['integration']['type'])
    except requests.exceptions.HTTPError as err:
        print(' Something went wrong. Code: {code}'.format(code=r.status_code), r.reason, jsonObj['integration']['id'])
