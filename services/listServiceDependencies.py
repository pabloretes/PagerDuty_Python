import http.client
import json

conn = http.client.HTTPSConnection("api.pagerduty.com")

def get_service_dependencies(API_Key, idBusinessService):
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': f"Token token={API_Key}"
        }

    conn.request("GET", f"/service_dependencies/business_services/{idBusinessService}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    jsonObj = json.loads(data)
    return jsonObj
