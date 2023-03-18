import services.listBusinessServices

def findBusinessServicebyName(API_KEY, businessServiceName):
    objBServices = services.listBusinessServices.getServices(API_KEY)
    for bs in objBServices['business_services']:
        if bs['name'] == businessServiceName:
            return(bs['id'])