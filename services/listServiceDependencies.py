import requests
import services.listBusinessServices

def getService_Dependecies(ApiKey):
    listObj = services.listBusinessServices.getServices(ApiKey)
    for obj in listObj['business_services']:
        idBusinessService = obj['id']
        url = 'https://api.pagerduty.com/service_dependencies/business_services/{id}'.format(id=idBusinessService)

        headers = {
            'Content-Type': "application/json",
            'Accept': "application/vnd.pagerduty+json;version=2",
            'Authorization': f"Token token={ApiKey}"
        }

        payload = {
            'query': ''
        }

        r = requests.get(url, headers=headers, params=payload)
        jsonObj = r.json()
        return (jsonObj)