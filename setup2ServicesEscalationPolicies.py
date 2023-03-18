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
from services import createBusinessService,listBusinessServices,deleteBusinessServices,createService,deleteServices,listServices

############################
# Author: Pablo Retes
# March 2023

#In this script:
# Old Services are deleted
# Old Business Services are deleted
# New Services are created
# New Business Services are created
# To assign to the team that owns the Business Service

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

#######################################################################
#To reset all
#Delete Business Services
print("\n")
listObjects = listBusinessServices.getServices(API_KEY)
deleteBusinessServices.delete_business_services(API_KEY,listObjects)

#Delete Technical Services
print("\n")
listObjects = listServices.getServices(API_KEY)
deleteServices.delete_services(API_KEY,listObjects)

#################################################################################
#Create Business Service
print("\n")
createBusinessService.create_business_service(API_KEY)

#Create Service
print("\n")
createService.create_service(API_KEY)