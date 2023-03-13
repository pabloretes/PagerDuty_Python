import listTeams

API_KEY = 'u+M1ooHmsW2rTsW7saCg'
objTeams = listTeams.list_teams(API_KEY)

for team in objTeams['teams']:
    print(team)

