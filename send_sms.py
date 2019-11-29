import os
from twilio.rest import Client

account_sid = "ACb35c4ced6bd52b9f82f7ef5e1d5331d7"
auth_token = "2de34a34c3e12272895d2b923661b426"

client = Client(account_sid, auth_token)

message = client.messages.create(
        to = "+16476878190",
        from_ = "+17059990096",
        body = "Hello How are you!"
)

print(message.sid)