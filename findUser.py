import apiKey
import listUsers

API_KEY = apiKey.getApiKey('../NoGithub.txt')

def findUserbyName(userName):
    objUsers = listUsers.list_users(API_KEY)
    for user in objUsers['users']:
        if user['name'] == userName:
            return(user['id'])
