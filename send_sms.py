# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6f915ff0db7e1645589f9156********'
auth_token = '923b8bf7f6fe5f48e4*************'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello Darkness my old friend.",
                     from_='+16788205***',
                     to='+918638******'
                 )

print(message.sid)