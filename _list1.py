import apiKey
import listTeams
import listUsers
import listTags
from schedules import listSchedules

############################
# Author: Pablo Retes
# March 2023

#In this script:

# Team List
# User List
# Tag List

##############################

API_KEY = apiKey.getApiKey('NoGithub.txt')
listObj = ''

####################################################################
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


