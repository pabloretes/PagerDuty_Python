###############################################
# Initial setup: Just run one time
# Author: Pablo Retes
# March 2023

import createUser
import apiKey
import createTeam
from schedules import createSchedule
from services import createBusinessService
from escalationPolicies import createEscalationPolicy
from services import createService,createServiceDependecies,createServiceDependecies,findServices
from integrations import createIntegration

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

################################################

# Create Teams
print("\n")
nameFile = 'initialTeamslist.csv'
createTeam.create_team(API_KEY,nameFile)

# #Create Usuarios
print("\n")
nameFile = 'initialUsersList.csv'
createUser.create_user(API_KEY, nameFile)

#Create Schedules
print("\n")
createSchedule.create_shedule(API_KEY)

#Create Business Service
print("\n")
nameFile = 'initialBusinessServicesList.csv'
createBusinessService.create_business_service(API_KEY,nameFile)

#Create Escalation Policy
print("\n")
teamName = 'Central Engineering and Ops Team'
createEscalationPolicy.create_escalation_policy(API_KEY,teamName)

#Create Service
print("\n")
nameFile = 'initialServices.csv'
createService.create_service(API_KEY,nameFile)

#Create Service Dependencies
print("\n")
nameFile = 'initialServices.csv'
createServiceDependecies.create_service_dependencies(API_KEY,nameFile)

#Create Service integration
print("\n")
idService = findServices.findServicebyName(API_KEY,'ACME Payment Processing service')
createIntegration.create_email_integration(API_KEY,idService)
