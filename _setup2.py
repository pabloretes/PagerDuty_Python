import apiKey
from schedules import createSchedule
from services import createBusinessService,createService,createServiceDependecies
from escalationPolicies import createEscalationPolicy

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

#Create Schedules
print("\n")
createSchedule.create_shedule(API_KEY)

#Create Business Service
print("\n")
createBusinessService.create_business_service(API_KEY)

#Create Escalation Policy
print("\n")
createEscalationPolicy.create_escalation_policy(API_KEY)

#Create Service
print("\n")
createService.create_service(API_KEY)

#Create Service Dependencies
print("\n")
createServiceDependecies.create_service_dependencies(API_KEY)

