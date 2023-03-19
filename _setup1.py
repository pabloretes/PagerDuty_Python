import createUser
import apiKey
import createTeam
from schedules import createSchedule

############################
# Author: Pablo Retes
# March 2023

#In this script:

# New Teams are created
# New Tags for the team are created
# New users are created
# New users are assigned to teams
# New On-Call Schedules are created
# New users are assigned to schedule shifts

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

#######################################################################

#To create all

# Create Teams
print("\n")
createTeam.create_team(API_KEY)

# #Create Usuarios
print("\n")
createUser.create_user(API_KEY)

