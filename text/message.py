from twilio.rest import Client
import os
phone_number = os.getenv("PHONE_NUMBER")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="sms_order_confirmation",
    from_= "+447460077297",
    to= phone_number,
)

print(message.sid)
