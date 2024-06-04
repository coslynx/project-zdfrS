import requests
from api_integration.kopeechka_api import verify_email

def email_verification(email):
    if verify_email(email):
        return True
    else:
        return False