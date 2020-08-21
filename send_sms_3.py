from twilio.rest import Client
from credentials import account_sid, auth_token, ph_number, my_twilio

client = Client(account_sid, auth_token)

my_msg = ''.join([" Good Morning " for i in range(3)])

message = client.messages.create(to=ph_number, from_=my_twilio,
                                     body=my_msg)
print(message.sid)
print(message)