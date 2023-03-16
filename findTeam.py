import apiKey
import listTeams

API_KEY = apiKey.getApiKey('NoGithub.txt')

def findTeambyName(teamName):
    objTeams = listTeams.list_teams()
    for team in objTeams['teams']:
        if team['name'] == teamName:
            return(team['id'])
