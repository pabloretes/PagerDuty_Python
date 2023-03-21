
import deleteTags
import deleteUser
import listTags
import listUsers
import apiKey
import listTeams
import deleteTeam
from schedules import deleteSchedules,listSchedules
from escalationPolicies import deleteEscalationPolicy,listEscalationPolicies
from services import deleteServices,listServices,deleteBusinessServices,listBusinessServices

############################
# Author: Pablo Retes
# March 2023

#In this script:

# Old Users are deleted
# Old Tags are deleted
# Old Technical Services are deleted
# Old Escalation Policies are deleted
# Old On-Call Schedules are deleted
# Old Teams are deleted
# Old Business Services are deleted

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

###############################################

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

#Delete Technical Services
print("\n")
listObjects = listServices.getServices(API_KEY)
deleteServices.delete_services(API_KEY,listObjects)

#Delete Escalation Policies
print("\n")
listObjects = listEscalationPolicies.getEscalationPolicies(API_KEY)
deleteEscalationPolicy.delete_escalation_policies(API_KEY,listObjects)

#Delete Schedules
print("\n")
listObjects = listSchedules.getSchedules(API_KEY)
deleteSchedules.delete_schedules(API_KEY, listObjects)

#Delete Teams
print("\n")
objTeams = listTeams.list_teams(API_KEY)
for team in objTeams['teams']:
    deleteTeam.delete_team(API_KEY, team['id'], team['name'])

#Delete Business Services
print("\n")
listObjects = listBusinessServices.getServices(API_KEY)
deleteBusinessServices.delete_business_services(API_KEY,listObjects)


