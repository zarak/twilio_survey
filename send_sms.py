# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to=os.environ["MY_PHONE_NUMBER"],
    from_="+16072892221",
    body="Hi! I’m the David Kidder chatbot!\n
    have you generated any new ideas?")
