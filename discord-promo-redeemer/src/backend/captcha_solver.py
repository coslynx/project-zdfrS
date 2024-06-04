import requests

class CaptchaSolver:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://fcaptcha.lol/api/solve"
    
    def solve_captcha(self, captcha_image_url):
        payload = {
            "api_key": self.api_key,
            "image_url": captcha_image_url
        }
        
        try:
            response = requests.post(self.base_url, json=payload)
            if response.status_code == 200:
                captcha_solution = response.json()["solution"]
                return captcha_solution
            else:
                return "Error solving captcha: {}".format(response.text)
        except requests.exceptions.RequestException as e:
            return "Error solving captcha: {}".format(e)