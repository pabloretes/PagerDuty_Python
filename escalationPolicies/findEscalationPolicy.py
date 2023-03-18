import escalationPolicies.listEscalationPolicies

def findEscalationPolicyByName(API_KEY, name):
    listObjects = escalationPolicies.listEscalationPolicies.getEscalationPolicies(API_KEY)
    for obj in listObjects['escalation_policies']:
        if obj['name'] == name:
            return(obj['id'])