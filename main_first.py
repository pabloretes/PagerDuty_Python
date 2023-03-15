import createUser
import deleteUser
import deleteTeam
import createTeam
import listTeams
import listUsers
import apiKey


############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = apiKey.getApiKey()
objTeams = listTeams.list_teams(API_KEY)
objUsers = listUsers.list_users(API_KEY)

#######################################################################
#Eliminar Teams
print("\nListado de Teams Eliminados:")
for team in objTeams['teams']:
    print(f" {deleteTeam.delete_team(API_KEY, team['id'])}")
print(f" Se eliminaron {len(objTeams['teams'])} Team(s)")

#Eliminar Usuarios
print("\nListado de Usuarios Eliminados:")
for user in objUsers['users']:
    if user["id"] == "PP1VDH4":
        print(f" Este no se borra: {user['id']} {user['name']}")
    else:
        print(f" {deleteUser.delete_user(API_KEY, user['id'])}",user["name"])
print(f" Se eliminaron {len(objUsers['users'])-1} usuario(s)")

######################################################################
# Crear Teams
createTeam.create_team(API_KEY)
objTeams = listTeams.list_teams(API_KEY)
print(f"\nSe crearon {len(objTeams['teams'])} Team(s)")

# Crear Usuarios
createUser.create_user(API_KEY)
objUsers = listUsers.list_users(API_KEY)
print(f"Se crearon {len(objUsers['users'])-1} Usuario(s)")

######################################################################


#Listar Teams
print("\nListado de Teams Encontrados:")
for team in objTeams['teams']:
    print(f" {team['id']}",team['name'])
print(f" Se encontraron {len(objTeams['teams'])} Team(s)")

#Listar Usuarios
print("\nListado de Usuarios Encontrados:")
for user in objUsers['users']:
    print(f" {user['id']}, {user['name']}, {user['email']}")
print(f" Se encontraron {len(objUsers['users'])} usuario(s)")

