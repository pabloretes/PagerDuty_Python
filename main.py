import deleteUser
import listTeams
import listUsers
import deleteTeam

############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = 'u+M1ooHmsW2rTsW7saCg' # se reemplaza
objTeams = listTeams.list_teams(API_KEY)
objUsers = listUsers.list_users(API_KEY)

######################################################################
#Listar Teams
print("\nListado de Teams Existentes:")
for team in objTeams['teams']:
    print(team["id"],team["name"])
print(f" Se encontraron {len(objTeams['teams'])} Team(s)")

#Listar Usuarios
print("\nListado de Usuarios Existentes:")
for user in objUsers['users']:
    print(user["id"], user["name"])
print(f" Se encontraron {len(objUsers['users'])} usuario(s)")

#######################################################################
#Eliminar Teams
print("\nListado de Teams Eliminados:")
for team in objTeams['teams']:
    print(deleteTeam.delete_team(API_KEY, team["id"]))
print(f" Se eliminaron {len(objTeams['teams'])} Team(s)")

#Eliminar Usuarios
print("\nListado de Usuarios Eliminados:")
for user in objUsers['users']:
    if user["id"] == "PP1VDH4":
        print(f" Este no se borra: {user['id']} {user['name']}")
    else:
        print(deleteUser.delete_user(API_KEY, user["id"]),user["name"])
print(f" Se eliminaron {len(objUsers['users'])-1} usuario(s)")

#######################################################################
# Crear Teams

# Crear Usuarios
