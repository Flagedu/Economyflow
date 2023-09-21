import requests
import simplejson
import json

url = "https://trader.alvexo.com/web-api/v3/lead/register-aff?bn_cmp=2757470&t_cre=TradeBitcointest&bn_source=economyflow"


token = "fwqass2rfa=2rNDMzOWFzY29pMW5iczIyZmVhc3ZlMzVlYXNkZmFsdmV4bw=="
authorization = 'Bearer %s' %token
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"

data = {
    "inputs[email]": "amirtest12@gmail.com",
    "inputs[fullName]": "amir test",
    "inputs[telephone]": "8801623539984",
    "inputs[password]": "Nstu1234!@",
    "inputs[demolive]": 1,
    "inputs[countryID]": "BD",
    "inputs[language]": "en",
    "inputs[token]": token,
    "inputs[clientIP]": "167.172.41.255",
    "inputs[lpID]": 2659,
    "inputs[clientUseragent]": user_agent
}

r = requests.post(url, headers=headers, data=data)
json_data = json.loads(r.content.decode('utf-8'))
print(json_data)