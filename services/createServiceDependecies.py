import requests
import json
import services.findBusinessService
import services.findServices
import csv

def create_service_dependencies(API_KEY):

    with open("services/servicesList.csv", newline='') as csvServices:
        fileReader = csv.reader(csvServices)
        for serviceData in fileReader:
            idBusinessService = services.findBusinessService.findBusinessServicebyName(API_KEY, serviceData[2])
            idService = services.findServices.findServicebyName(API_KEY, serviceData[1])
            payload ={
              "relationships": [
                {
                  "supporting_service": {
                    "id": idService,
                    "type": "technical_service_reference"
                  },
                  "dependent_service": {
                    "id": idBusinessService,
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

            url = 'https://api.pagerduty.com/service_dependencies/associate'

            try:
                r = requests.post(url, headers=headers, data=json.dumps(payload))
                r.raise_for_status()
                jsonObj = r.json()
                print(' Code: {code},'.format(code=r.status_code), f'Creating Service dependencies...for business service --> {idBusinessService}:'
                                                                   f'technical service: {idService}')

            except requests.exceptions.HTTPError as err:
                print(' Something went wrong. Code: {code} Service dependencies'.format(code=r.status_code), r.reason)
