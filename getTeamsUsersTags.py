import apiKey
import listTeams
import listUsers
import listTags

############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = apiKey.getApiKey('NoGithub.txt')
objTeams = listTeams.list_teams()
objUsers = listUsers.list_users()
objTags = listTags.getTags()

#####################################################################
#Listar Teams
print("Team List:")
for team in objTeams['teams']:
    print(f" {team['id']}",team['name'])
print(f" {len(objTeams['teams'])} Team(s) founded")

#Listar Usuarios
print("\nUser List:")

for user in objUsers['users']:
    print(f" {user['id']}, {user['name']}, {user['email']}")
print(f" {len(objUsers['users'])} users(s) founded")

print("\nTag List:")
for tag in objTags['tags']:
    print(tag['id'], tag['label'])
