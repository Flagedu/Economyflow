import simplejson
import json
import requests
import hashlib
import time
from datetime import datetime

def make_sha1(s, encoding='utf-8'):
        return hashlib.sha1(s.encode(encoding)).hexdigest()

def create_access_key(time):
    PARTNER_ID = '25974691'
    PARTNER_SECRET_KEY = '94e1979cbeee02d5fc820dfce9b155bf1a29dcb58a07d393899e144d7af93b10'
    TIME = time

    concatenated_string = PARTNER_ID + str(TIME) + PARTNER_SECRET_KEY
    ACCESS_KEY = make_sha1(concatenated_string)
    return ACCESS_KEY

def get_token():
    url = 'https://mena-evest.pandats-api.io/api/v3/authorization'

    l_time = int(time.time())
    access_key = create_access_key(l_time)

    data = {
        'partnerId': '25974691',
        'time': str(l_time),
        'accessKey': access_key,
    }

    data_json = simplejson.dumps(data)

    headers = {
        'Content-Type': 'application/json',
    }

    r = requests.post(url, headers=headers, data=data_json)

    json_data = json.loads(r.content.decode('utf-8'))

    token = json_data['data']['token']
    return token

def get_customers():
    token = get_token()
    url = 'https://mena-evest.pandats-api.io/api/v3/customers?page=1&limit=1'

    authorization = 'Bearer %s' %token

    headers = {
        'Content-Type': 'application/json',
        'Authorization': authorization
    }

    r = requests.get(url, headers=headers)

    json_data = json.loads(r.content.decode('utf-8'))

    return json_data

customers = get_customers()
print(customers)
# datas = customers["data"]

# final_list = []

# for d in datas:
#     amount = d["amount"]
#     ftd = d["ftd"]
#     createdTime = d["createdTime"]
#     createdTime = createdTime.split("T")[0]
#     compared_date = "2021-05-31"
#     convertedDate = datetime.strptime(createdTime, '%Y-%m-%d')
#     comparedDateObj = datetime.strptime(compared_date, '%Y-%m-%d')
#     if convertedDate > comparedDateObj and amount >= 250:
#         final_list.append(d)


# print(len(final_list))