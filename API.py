import requests
import json

# # Variables
Itemsinpage = "100"
PageNumber = ""
keyword_list = ["Schedule", "power outage", "Server Down"]


# # Headers and Parameters
parameters = {
    "itemsInPage":Itemsinpage,
    "Page":PageNumber
}

Headers = {
    "X-API-KEY" : "2e6ab90f97734051bfc4b6a45823215a"
}

# # getting response from the Atera Url
response = requests.get("https://app.atera.com/api/v3/tickets", headers=Headers, params=parameters)
print ("Successful! Status Code:{}".format(response.status_code))

# # Function to convert Scrapped data to Proper Json format
def jprint(obj):
    text = json.dumps(obj, sort_keys=True , indent=4)
    return text

# # Getting all ticket Items as Ticket_Items
Ticket_Items = response.json()["items"]
#Example : print(Ticket_Items)


# # Getting AllValues of Key Items from Response
def Get_Values(Key):
    Values = []
    Ticket_Items = response.json()["items"]
    for Ticket_Item in Ticket_Items:
        Values.append(Ticket_Item[Key])
    return Values
# Example : print(jprint(Get_Values("TicketStatus")))


# # Getting All Open tickets NOT send by System (REAL OPEN TICKETS and TICKET TITLES)
Real_Open_Tickets = []
Real_Open_Tickets_Titles = []

while(len(Get_Values("TicketID")) >> 0):
    if Get_Values
    for value in Get_Values("TicketStatus")
    for Ticket_Item in Ticket_Items:
        Ticket_Status = Ticket_Item["TicketStatus"]
        Ticket_EnsUserLastName = Ticket_Item["EndUserLastName"]
        Ticket_Title = Ticket_Item["TicketTitle"]
        if Ticket_EnsUserLastName != "System":
            Real_Open_Tickets.append(Ticket_Item)
            Real_Open_Tickets_Titles.append(Ticket_Title)

# # print(jprint(Real_Open_Tickets_Titles))



# # Printing tickets with specific keywords

# # Keyword_list is in the variable section at the top
for Ticket_Item in Real_Open_Tickets:
    Ticket_ID = Ticket_Item["TicketID"]
    Ticket_Title = Ticket_Item["TicketTitle"]
    if any(word in Ticket_Title for word in keyword_list):
        print("Ticket ID is: "+ Ticket_ID + " and Ticket Title is: " + Ticket_Title)

print (jprint(Real_Open_Tickets_Titles))




# # Ticket_Status == "Open" and 
