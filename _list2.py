import apiKey
from schedules import listSchedules
from escalationPolicies import listEscalationPolicies
from services import listServices,listBusinessServices,listServiceDependencies


############################
# Author: Pablo Retes
# March 2023

#In this script:

# schedules List
# business services List
# escalation policies List
# services List
# service dependencies List

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')
listObj = ''

###################################################################

#Listar schedules
listObj = listSchedules.getSchedules(API_KEY)
print("\nSchedule List:")
for obj in listObj['schedules']:
    print(obj['id'], obj['name'])

#to list business services
listBServices = listBusinessServices.getServices(API_KEY)
print("\nBusiness Services List:")
for obj in listBServices['business_services']:
    print(obj['id'], obj['name'],'|',obj['description'])

#Listar escalation policies
listObj = listEscalationPolicies.getEscalationPolicies(API_KEY)
print("\nEscalation Policies List:")
for obj in listObj['escalation_policies']:
    print(obj['id'], obj['name'])

#Listar services
ObjServices = listServices.getServices(API_KEY)
print("\nServices List:")
for obj in ObjServices['services']:
    print(obj['id'], obj['name'],'|',obj['description'])

#Listar service dependencies
print("\nServices Dependencies List:")
for objBService in listBServices['business_services']:
    idBS = objBService['id']
    ObjServicesDependencies = listServiceDependencies.get_service_dependencies(API_KEY,idBS)
    for obj in ObjServicesDependencies['relationships']:
        print(f'Business Service has :{obj["dependent_service"]["id"]}',f'has supporting service : {obj["supporting_service"]["id"]}')