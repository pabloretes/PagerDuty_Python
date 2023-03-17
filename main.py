import createUser
import deleteTags
import deleteUser
import listUsers
import apiKey
import listTeams
import deleteTeam
import createTeam
from schedules import deleteSchedules,listSchedules,createSchedule

############################
# Author: Pablo Retes
# March 2023
############################

API_KEY = apiKey.getApiKey('NoGithub.txt')
objTeams = listTeams.list_teams()
objUsers = listUsers.list_users(API_KEY)

# #######################################################################
# #To reset all
# #Delete Teams
# for team in objTeams['teams']:
#     deleteTeam.delete_team(API_KEY, team['id'], team['name'])
#
# #Delete users
# print("\n")
# for user in objUsers['users']:
#     if user["id"] == "PP1VDH4":
#         print(f" This is mine: {user['id']} {user['name']}")
#     else:
#         deleteUser.delete_user(API_KEY, user['id'], user['name'])
#
# #Delete Tags
# print("\n")
# deleteTags.delete_tags()
#
#Delete Schedules
print("\n")
listObjects = listSchedules.getSchedules(API_KEY)
deleteSchedules.delete_schedules(API_KEY, listObjects)
# ######################################################################
# #To create all
# # Create Teams
# print("\n")
# createTeam.create_team(API_KEY)
#
# # Create Usuarios
# print("\n")
# createUser.create_user(API_KEY)

# Create Schedules
print("\n")
createSchedule.create_shedule(API_KEY)



######################################################################

