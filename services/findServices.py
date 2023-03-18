import services.listServices

def findServicebyName(API_KEY, ServiceName):
    objServices = services.listServices.getServices(API_KEY)
    for service in objServices['services']:
        if service['name'] == ServiceName:
            return(service['id'])