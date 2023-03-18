import listTeams

def findTeambyName(API_KEY,teamName):
    objTeams = listTeams.list_teams(API_KEY)
    for team in objTeams['teams']:
        if team['name'] == teamName:
            return(team['id'])
