import schedules.listSchedules

def findSchedulebyName(API_KEY, ScheduleName):
    objSchedules = schedules.listSchedules.getSchedules(API_KEY)
    for service in objSchedules['schedules']:
        if service['name'] == ScheduleName:
            return(service['id'])