import apiKey
from services import createBusinessService,listBusinessServices,deleteBusinessServices,createService,deleteServices,listServices,createServiceDependecies
from escalationPolicies import createEscalationPolicy,listEscalationPolicies,deleteEscalationPolicy

############################
# Author: Pablo Retes
# March 2023

#In this script:
# Old Services are deleted
# Old Business Services are deleted
# Old Services Dependecies are deleted
# Old Escalation Policies are deleted

# New Business Services are created
# Team that owns of the Business Service assigned
# New Escalation Policies are created with Policies Rules and Schedule & user assigned
# New Services are created
# New Service dependencies are created for business service

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

#Delete Escalation Policies
print("\n")
listObjects = listEscalationPolicies.getEscalationPolicies(API_KEY)
deleteEscalationPolicy.delete_escalation_policies(API_KEY,listObjects)

#################################################################################
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

