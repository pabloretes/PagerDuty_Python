import createUser
import deleteUser
import listUsers
import apiKey
import listTeams
import deleteTeam
import createTeam

############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = apiKey.getApiKey()
objTeams = listTeams.list_teams(API_KEY)
objUsers = listUsers.list_users(API_KEY)

#######################################################################
#Eliminar Teams
for team in objTeams['teams']:
    deleteTeam.delete_team(API_KEY, team['id'], team['name'])

#Eliminar Usuarios
print("\n")
for user in objUsers['users']:
    if user["id"] == "PP1VDH4":
        print(f" This is mine: {user['id']} {user['name']}")
    else:
        deleteUser.delete_user(API_KEY, user['id'], user['name'])
######################################################################
# Crear Teams
print("\n")
createTeam.create_team(API_KEY)

# Crear Usuarios
print("\n")
createUser.create_user(API_KEY)
objUsers = listUsers.list_users(API_KEY)
######################################################################

# #Listar Teams
# print("\nListado de Teams Encontrados:")
# for team in objTeams['teams']:
#     print(f" {team['id']}",team['name'])
# print(f" Se encontraron {len(objTeams['teams'])} Team(s)")
#
# #Listar Usuarios
# print("\nListado de Usuarios Encontrados:")
# for user in objUsers['users']:
#     print(f" {user['id']}, {user['name']}, {user['email']}")
# print(f" Se encontraron {len(objUsers['users'])} usuario(s)")
#
