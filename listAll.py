import apiKey
import listTeams
import listUsers
import listTags
from schedules import listSchedules
from escalationPolicies import listEscalationPolicies
from services import listServices,listBusinessServices


############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = apiKey.getApiKey('NoGithub.txt')
listObj = ''

#####################################################################
#Listar Teams
listObj = listTeams.list_teams(API_KEY)
print("Team List:")
for team in listObj['teams']:
    print(f" {team['id']}",team['name'])

#Listar Usuarios
listObj = listUsers.list_users(API_KEY)
print("\nUser List:")
for user in listObj['users']:
    print(f" {user['id']}, {user['name']}, {user['email']}")

#Listar Tags
listObj = listTags.getTags(API_KEY)
print("\nTag List:")
for tag in listObj['tags']:
    print(tag['id'], tag['label'])

#Listar schedules
listObj = listSchedules.getSchedules(API_KEY)
print("\nSchedule List:")
for obj in listObj['schedules']:
    print(obj['id'], obj['name'])

#Listar escalation policies
listObj = listEscalationPolicies.getEscalationPolicies(API_KEY)
print("\nEscalation Policies List:")
for obj in listObj['escalation_policies']:
    print(obj['id'], obj['name'])

#to list business services
listObj = listBusinessServices.getServices(API_KEY)
print("\nBusiness Services List:")
for obj in listObj['business_services']:
    print(obj['id'], obj['name'],'|',obj['description'])

#Listar services
listObj = listServices.getServices(API_KEY)
print("\nServices List:")
for obj in listObj['services']:
    print(obj['id'], obj['name'],'|',obj['description'])