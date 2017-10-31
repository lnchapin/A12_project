from twilio.rest import Client
import os
from settings import TWILIO_NUMBER, AUTH_TOKEN, ACCOUNT_SID, JOSCELYN

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    to=JOSCELYN,
    from_=TWILIO_NUMBER,
    body="Hello from Python!")

print(message.sid)