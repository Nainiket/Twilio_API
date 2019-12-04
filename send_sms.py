from Scrap import Get_All_Agents, Get_Offline_Servers,jprint
import os
from twilio.rest import Client

account_sid = "ACb35c4ced6bd52b9f82f7ef5e1d5331d7"
auth_token = "2de34a34c3e12272895d2b923661b426"

client = Client(account_sid, auth_token)

a = (Get_Offline_Servers())
for i in a:
    print(i)
    message = client.messages.create(
            to = "+17057702540",
            from_ = "+17059990096",
            body = i
        )