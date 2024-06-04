import requests

class FcaptchaLolApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://fcaptcha.lol/api/v1"

    def solve_captcha(self, image_url):
        endpoint = "/solve_captcha"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "image_url": image_url
        }
        response = requests.post(self.base_url + endpoint, headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json()["captcha_text"]
        else:
            return None