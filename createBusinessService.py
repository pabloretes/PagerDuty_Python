import http.client

conn = http.client.HTTPSConnection("api.pagerduty.com")

payload = "{\n  \"business_service\": {\n    \"name\": \"Self-serve mobile checkout\",\n    \"description\": \"Checkout service for our mobile clients\",\n    \"point_of_contact\": \"PagerDuty Admin\",\n    \"team\": {\n      \"id\": \"PN8BUIA\"\n    }\n  }\n}"

headers = {
    'Content-Type': "application/json",
    'Accept': "application/vnd.pagerduty+json;version=2",
    'Authorization': "Token token=u+M1ooHmsW2rTsW7saCg"
    }

conn.request("POST", "/business_services", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))