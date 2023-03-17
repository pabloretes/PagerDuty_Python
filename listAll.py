import apiKey
import listTeams
import listUsers
import listTags
from schedules import listSchedules

############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = apiKey.getApiKey('NoGithub.txt')
listObj = ''

#####################################################################
#Listar Teams
listObj = listTeams.list_teams()
print("Team List:")
for team in listObj['teams']:
    print(f" {team['id']}",team['name'])

#Listar Usuarios
listObj = listUsers.list_users(API_KEY)
print("\nUser List:")
for user in listObj['users']:
    print(f" {user['id']}, {user['name']}, {user['email']}")

#Listar Tags
listObj = listTags.getTags()
print("\nTag List:")
for tag in listObj['tags']:
    print(tag['id'], tag['label'])

#Listar schedules
listObj = listSchedules.getSchedules(API_KEY)
print("\nSchedule List:")
for obj in listObj['schedules']:
    print(obj['id'], obj['name'])