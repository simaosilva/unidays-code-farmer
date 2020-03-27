import requests
import json
from time import sleep
import urllib3
from datetime import datetime

def grab_captcha(api_key, site_key):
    url = "https://www.myunidays.com/"
    successful_captcha_post = False
    while not successful_captcha_post:
        try:
            captcha_id = \
                requests.post(
                    "http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(
                        api_key, site_key, url)).text.split('|')[1]
            successful_captcha_post = True
        except requests.exceptions.Timeout:
            # Timeout, server took too long to respond.
            print(
                f"[{str(datetime.now())}] The server did not send any data in the allotted amount of time,retrying captcha post request...")
            continue
        except Exception as e:
            # Handle other exceptions.
            print(f"[{str(datetime.now())}] Unknown exception {e} retrying captcha post request...")
            continue
    successful_grab_response = False
    while not successful_grab_response:
        try:
            recaptcha_answer = requests.get(
                "http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, captcha_id)).text
            successful_grab_response = True
        except requests.exceptions.Timeout:
            # Timeout, server took too long to respond.
            print(f"[{str(datetime.now())}] The server did not send any data in the allotted amount of time,retrying captcha get request...")
            continue
        except Exception as e:
            # Handle other exceptions.
            print(f"[{str(datetime.now())}] Unknown exception {e} retrying captcha post request...")
            continue
    print(f"[{str(datetime.now())}] Solving captcha...")
    while 'CAPCHA_NOT_READY' in recaptcha_answer:
        sleep(2)
        try:
            recaptcha_answer = requests.get(
                "http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, captcha_id)).text
        except requests.exceptions.Timeout:
            # Timeout, server took too long to respond.
            print(f"[{str(datetime.now())}] The server did not send any data in the allotted amount of time,retrying captcha get request...")
            continue
        except Exception as e:
            # Handle other exceptions.
            print(f"[{str(datetime.now())}] Unknown exception {e} retrying captcha post request...")
            continue
    recaptcha_answer = recaptcha_answer.split('|')[1]
    print(f"[{str(datetime.now())}] Captcha Solved!")
    return recaptcha_answer


class UnidaysCodeFarmer:
    def __init__(self):
        self.site = input(f"[{str(datetime.now())}] Please enter here what site you want to farm codes for: ").lower()
        self.number_of_codes_generated = 0
        self.s = requests.session()
        self.site_key = '6Ld9uqgUAAAAAKiIVOqkxm7l-Vmpe9F-9ORCOUQg'
        self.s.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
            "Origin": "https://www.myunidays.com",
            "ud-source": "www"
        }
        with open("setting.json") as account_file:
            account_data = json.load(account_file)
            self.account_login = account_data['email']
            self.account_password = account_data['password']
            self.account_region = account_data['region']
            self.captcha_api_key = account_data['2captcha_api_key']

    def login(self):
        captcha = grab_captcha(self.captcha_api_key, self.site_key)
        payload = {
            'QueuedPath': f'/{self.account_region}/{self.account_region.lower()}-{self.account_region}',
            'EmailAddress': self.account_login,
            'Password': self.account_password,
            'g-recaptcha-response': captcha,
            'GTokenResponse': captcha
        }
        login_url = f'https://account.myunidays.com/{self.account_region}/{self.account_region.lower()}-{self.account_region}/account/log-in'
        login_response = self.s.post(login_url, data=payload, verify=False)
        if login_response.status_code == 200:
            print(f"[{str(datetime.now())}] Successfully logged in!")
        else:
            print(f"[{str(datetime.now())}] Check your credentials")

    def grab_code(self):
        open(f"{self.site}_discount_codes.txt", "w")
        while True:
            payload = {
                "forceNew": "true"
            }
            code_response = self.s.post(f"https://perks.myunidays.com/access/{self.site}/online", data=payload, verify=False)
            if code_response.status_code == 200:
                self.number_of_codes_generated += 1
                discount_code = code_response.json()["code"]
                print(f"[{str(datetime.now())}] Got code {discount_code}, you have generated {str(self.number_of_codes_generated)} already!")
                with open(f"{self.site}_discount_codes.txt", "a") as f:
                    f.write(discount_code)
                    f.close()
            else:
                print(f"[{str(datetime.now())}] Error grabbing code")
            print(f"[{str(datetime.now())}] Waiting 60 minutes until trying to grab new code")
            sleep(3600)


if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    code_farmer = UnidaysCodeFarmer()
    code_farmer.login()
    code_farmer.grab_code()
    print(f"[{str(datetime.now())}] All codes successfully grabbed")
