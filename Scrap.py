import requests
import json

# # Variables
Itemsinpage = ""
for i in (1,10):
    PageNumber = i
print(PageNumber)
# # Headers and Parameters
parameters = {
    "itemsInPage":Itemsinpage,
    "Page":PageNumber,
    "machineName":"Server"
}
Headers = {
    "X-API-KEY" : "2e6ab90f97734051bfc4b6a45823215a",
    "Accept": "application/json"
}
# # getting response from the Atera Url
response = requests.get("https://app.atera.com/api/v3/agents", headers=Headers, params=parameters)
print ("Status Code:{}".format(response.status_code))

# # Function to convert Scrapped data to Proper Json format
def jprint(obj):
    text = json.dumps(obj, sort_keys=True , indent=4)
    return text

# # Printing Clean JSON Data or the Requested Page
# print(jprint(response.json()))

Agents_All = response.json()["items"]

print(len(Agents_All))
for agent in Agents_All:
    if agent["Monitored"] == True:
        print (agent["CustomerName"], agent["AgentName"])


# print(len(Agents_All))

# def Get_Server():
#     # Servers = {}
#     for agent in Agents_All:
#         if agent['SystemName'] == "SERVER":
#             print(agent["CustomerName"], agent["MachineName"])

# Get_Server()
# # print(Servers)