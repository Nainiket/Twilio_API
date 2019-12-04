import requests
import json


def Get_All_Agents():
    All_Agents = []
    # # Variables
    Itemsinpage = "50"
    for i in range(1,10):
        PageNumber = i
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
        # print ("Status Code:{}".format(response.status_code))
        All_Agents.append(response.json()["items"])
    return All_Agents

        # print(len(Agents_All))

def Get_Offline_Servers():        
    Offline_Servers = []
    for i in Get_All_Agents():
        for agent in i:
            if agent["Monitored"] == True and agent["Online"] == False:
                a = agent["CustomerName"] + agent["AgentName"] + "  IS OFFLINE"
                Offline_Servers.append(a) 
    return Offline_Servers

    # Function to convert Scrapped data to Proper Json format
def jprint(obj):
    text = json.dumps(obj, sort_keys=True , indent=4)
    return text

print (len(Get_Offline_Servers()))