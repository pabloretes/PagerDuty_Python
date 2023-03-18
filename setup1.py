import createUser
import deleteTags
import deleteUser
import listTags
import listUsers
import apiKey
import listTeams
import deleteTeam
import createTeam
from schedules import deleteSchedules,listSchedules,createSchedule

############################
# Author: Pablo Retes
# March 2023

#In this script:
# Old Teams are deleted
# Old Users are deleted
# Old Tags are deleted
# Old On-Call Schedules are deleted
# New Teams are created
# New Tags for the team are created
# New users are created
# New users are assigned to teams
# New On-Call Schedules are created
# New users are assigned to schedule shifts

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

#######################################################################
#To reset all
#Delete Teams
objTeams = listTeams.list_teams(API_KEY)
for team in objTeams['teams']:
    deleteTeam.delete_team(API_KEY, team['id'], team['name'])

#Delete users
print("\n")
objUsers = listUsers.list_users(API_KEY)
for user in objUsers['users']:
    if user["id"] == "PP1VDH4":
        print(f" This is mine: {user['id']} {user['name']}")
    else:
        deleteUser.delete_user(API_KEY, user['id'], user['name'])

#Delete Tags
print("\n")
listObjects = listTags.getTags(API_KEY)
deleteTags.delete_tags(API_KEY, listObjects)

#Delete Schedules
print("\n")
listObjects = listSchedules.getSchedules(API_KEY)
deleteSchedules.delete_schedules(API_KEY, listObjects)

######################################################################
#To create all

# Create Teams
print("\n")
createTeam.create_team(API_KEY)

# #Create Usuarios
print("\n")
createUser.create_user(API_KEY)

#Create Schedules
print("\n")
createSchedule.create_shedule(API_KEY)