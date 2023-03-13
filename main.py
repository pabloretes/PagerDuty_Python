import listTeams
import listUsers
import deleteTeams

API_KEY = 'u+M1ooHmsW2rTsW7saCg' # se reemplaza
objTeams = listTeams.list_teams(API_KEY)
objUsers = listUsers.list_users(API_KEY)

######################################################################
#Listar Teams
print("\n Listado de Teams Existentes:")
for team in objTeams['teams']:
    print(team)

#Listar Usuarios
print("\n Listado de Usuarios Existentes:")
for user in objUsers['users']:
    print(user)

#######################################################################
#Eliminar Teams
print("\n Listado de Teams Eliminados:")
for team in objTeams['teams']:
    print(deleteTeams.delete_team(API_KEY, team["id"]))




#Eliminar Usuarios




