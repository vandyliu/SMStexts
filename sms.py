import os
from twilio.base.exceptions import TwilioRestException
from twilio.twiml.messaging_response import MessagingResponse, Body, Media, Message
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
main_phone_number = '+17786545908'
sms_url = "https://sms-maps.azurewebsites.net/sms"

client = Client(account_sid, auth_token)

incoming_phone_numbers = client.incoming_phone_numbers.list(phone_number=main_phone_number, limit=5)
main_phone_number_resource = incoming_phone_numbers[0]


def valid_text(text_message, counter):
    if ";" in text_message:
        return None
    locations = text_message.split(";")
    if len(locations) != 2:
        return None
    return True

def sms_reply(string):
    resp = MessagingResponse()
    message = Message()
    message.body(string)
    resp.append(message)
    return str(resp)
