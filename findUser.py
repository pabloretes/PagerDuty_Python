import apiKey
import listUsers

def findUserbyName(ApiKey, userName):
    objUsers = listUsers.list_users(ApiKey)
    for user in objUsers['users']:
        if user['name'] == userName:
            return(user['id'])
