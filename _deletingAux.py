import apiKey
from schedules import deleteSchedules,listSchedules
from escalationPolicies import deleteEscalationPolicy,listEscalationPolicies
from services import deleteServices,listServices,deleteBusinessServices,listBusinessServices

######################################################################

API_KEY = apiKey.getApiKey('NoGithub.txt')

######################################################################
# Deleting just: Technical Services,Escalation Policies,Schedules
#                Business Services


def deleteServices_and_dependencies():
# Delete Technical Services
    print("\n")
    listObjects = listServices.getServices(API_KEY)
    deleteServices.delete_services(API_KEY, listObjects)

    # Delete Escalation Policies
    print("\n")
    listObjects = listEscalationPolicies.getEscalationPolicies(API_KEY)
    deleteEscalationPolicy.delete_escalation_policies(API_KEY, listObjects)

    # Delete Schedules
    print("\n")
    listObjects = listSchedules.getSchedules(API_KEY)
    deleteSchedules.delete_schedules(API_KEY, listObjects)

    # Delete Business Services
    print("\n")
    listObjects = listBusinessServices.getServices(API_KEY)
    deleteBusinessServices.delete_business_services(API_KEY, listObjects)


if __name__ == '__main__':
    deleteServices_and_dependencies()
