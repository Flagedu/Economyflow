import requests
import simplejson
import hashlib
import json
import time
import phonenumbers
from django.apps import apps
from .phone_code import phone_codes


def post_customer(full_name, phone, country_id, email):        
    url = "https://platform.revotracking.com/api/signup/procform"
    token = "2643889w34df345676ssdas323tgc738"
    headers = {
        "Content-Type": "application/json",
        "x-trackbox-username": "Economyflow",
        "x-trackbox-password": "Economyflow2806",
        "x-api-key": token,
    }
    password = "Aa12345"
    split_full_name = full_name.split(" ")
    firstname = split_full_name[0]
    lastname = split_full_name[1]
    parse_number = phonenumbers.parse(phone, country_id)
    number_is_valid = phonenumbers.is_valid_number(parse_number)
    if number_is_valid:
        format_number = phonenumbers.format_number(parse_number, phonenumbers.PhoneNumberFormat.E164)
        data = {
            "ai": "2958269",
            "ci": "9",
            "gi": "221",
            "userip": "118.179.134.11",
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password,
            "phone": format_number,
            "so": "AFF_2958269",
            "MPC_4": "Economyflow",
        }
        data_json = simplejson.dumps(data)
        print(data_json)
        r = requests.post(url, headers=headers, data=data_json)
        json_data = json.loads(r.content.decode('utf-8'))
        print(json_data)
        try:
            status = json_data["status"]
            data = json_data["data"]
            if status == True:
                create_user(
                    email, 
                    password,
                    country_id,
                    firstname,
                    lastname,
                    phone
                )
                print("USER INSERTER INTO DB")
        except:
            print("USER NOT INSERTED")
    else:
        print("Phone number not valid!")


def create_user(email, password, country, firstName, lastName, phone):
    UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
    ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')
    user = UserProfile.objects.create(
        email=email,
        phone=phone,
        country=country,
        firstName=firstName,
        lastName=lastName,
        campaign="custom_axia"
    )
    try:
        api_reg_type_obj = ApiRegistration.objects.get(type="axia")
        api_reg_type_obj.members.add(user)
    except:
        pass