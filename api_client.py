import requests
import json

class APIClient:
    def __init__(self):
        self.base_url = "yourwebsite url"
        self.token = None
    
    def login(self, apiKey, language="tr-tr", currency="TRY"):
        login_url = f"{self.base_url}/common/apiLogin"
        payload = {
            "apiKey": apiKey,
            "language": language,
            "currency": currency
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(login_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            self.token = data.get("wk_token")
            return self.token
        else:
            return None
    
    def get_orders(self):
        if not self.token:
            raise Exception("Token is missing. Please login first.")
        
        orders_url = f"{self.base_url}/customer/getOrders"
        payload = {
            "wk_token": self.token
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(orders_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        else:
            return None
