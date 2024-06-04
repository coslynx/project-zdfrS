import requests

class KopeechkaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.kopeechka.lol"

    def verify_email(self, email):
        endpoint = f"{self.base_url}/verify_email"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "email": email
        }

        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Failed to verify email: {response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"An error occurred: {str(e)}"}