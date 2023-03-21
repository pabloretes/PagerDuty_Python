import apiKey
from schedules import createSchedule
from services import createBusinessService,createService,createServiceDependecies,findServices
from escalationPolicies import createEscalationPolicy
from integrations import createIntegration

############################
# Author: Pablo Retes
# March 2023

#In this script:

# New On-Call Schedules are created
# New Business Services are created
# New Escalation Policies are created
# New Services are created
# New Service Dependencies are created

###############################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

###############################################
# Just one time execute in initial configuration
# #Create Schedules
# print("\n")
# createSchedule.create_shedule(API_KEY)

# #Create Business Service
# print("\n")
# nameFile = 'services/businessserviceslist.csv'
# createBusinessService.create_business_service(API_KEY,nameFile)

# Just one time execute in initial configuration
# #Create Escalation Policy
# print("\n")
# createEscalationPolicy.create_escalation_policy(API_KEY)

#Create Service
print("\n")
nameFile = 'services/servicesList.csv'
createService.create_service(API_KEY,nameFile)

#Create Service Dependencies
print("\n")
nameFile = 'services/servicesList.csv'
createServiceDependecies.create_service_dependencies(API_KEY,nameFile)

# Just one time execute in initial configuration
# #Create Service integration
# print("\n")
# idService = findServices.findServicebyName(API_KEY,'ACME Payment Processing service')
# createIntegration.create_email_integration(API_KEY,idService)
