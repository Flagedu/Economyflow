import requests
import simplejson
import hashlib
import json
import time
import base64

from django import forms
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.apps import apps
from django.contrib.gis.geoip2 import GeoIP2

import phonenumbers

from .phone_code import phone_codes


# ─── EVEST FORM ─────────────────────────────────────────────────────────────────
class EvestForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.params = kwargs.pop("params")
        self.phone = kwargs.pop("phone")
        self.page_slug = kwargs.pop("page_slug")
        self.ip = kwargs.pop("ip")
        self.account_used = kwargs.pop("account_used")
        super().__init__(*args, **kwargs)

    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    firstName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    country = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))

    def make_sha1(self, s, encoding='utf-8'):
        return hashlib.sha1(s.encode(encoding)).hexdigest()

    def create_access_key(self, time):
        if self.account_used == 0:
            PARTNER_ID = '25974691'
            PARTNER_SECRET_KEY = '94e1979cbeee02d5fc820dfce9b155bf1a29dcb58a07d393899e144d7af93b10'
        else:
            PARTNER_ID = '93883'
            PARTNER_SECRET_KEY = '77b919860abc787f8b269d8eb79dbbe96cc90650597d289bd6cf176a1b6add0d'
        TIME = time

        concatenated_string = PARTNER_ID + str(TIME) + PARTNER_SECRET_KEY
        ACCESS_KEY = self.make_sha1(concatenated_string)
        return ACCESS_KEY

    def get_token(self):
        url = 'https://mena-evest.pandats-api.io/api/v3/authorization'

        l_time = int(time.time())
        access_key = self.create_access_key(l_time)

        if self.account_used == 0:
            partner_id = "25974691"
        else:
            partner_id = "93883"

        data = {
            'partnerId': partner_id,
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

    def post_customer(self):
        token = self.get_token()
        
        url = 'https://mena-evest.pandats-api.io/api/v3/customers'

        authorization = 'Bearer %s' %token

        headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization
        }

        if self.params:
            params = self.params
        else:
            if self.account_used == 0:
                params = "partner_id=c1a486dd6c8f128d0be36f669aa221fe|referal_id=35075_398162_EF02|affiliate_id=35075|Aff_id=35075|src=https://economyflow.com"
            else:
                params = "partner_id=c1a486dd6c8f128d0be36f669aa221fe|referal_id=35430_459801_efppc|affiliate_id=35430|Aff_id=35430|src=https://economyflow.com"


        if self.cleaned_data.get("password"):
            password = self.cleaned_data.get("password")
        else:
            password = "nstu1234"

        data = {
            'email': self.cleaned_data.get("email"),
            'password': password,
            'country': self.cleaned_data.get("country"),
            'firstName': self.cleaned_data.get("firstName"),
            'lastName': self.cleaned_data.get("lastName"),
            'phone': self.phone,
            "referral": params,
            "ip": self.ip,
            "acceptPromotions": True,
            "acceptTermsAndConditions": True
        }

        data_json = simplejson.dumps(data)

        r = requests.post(url, headers=headers, data=data_json)
        json_data = json.loads(r.content.decode('utf-8'))
        #return json_data
        
        error = json_data.get("error", None)
        if error:
            error_msg = error[0].get("description", None)
            if error_msg:
                UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
                user_exists = UserProfile.objects.filter(email=self.cleaned_data.get("email")).exists()
                if not user_exists:
                    self.create_user(
                        self.cleaned_data.get("email"), 
                        self.cleaned_data.get("password"),
                        self.cleaned_data.get("country"),
                        self.cleaned_data.get("firstName"),
                        self.cleaned_data.get("lastName"),
                        self.phone,
                        self.ip,
                        False
                    )
                return False, error_msg


        try:
            status = json_data["data"]["status"]
            if status == "ok":
                self.create_user(
                    self.cleaned_data.get("email"), 
                    self.cleaned_data.get("password"),
                    self.cleaned_data.get("country"),
                    self.cleaned_data.get("firstName"),
                    self.cleaned_data.get("lastName"),
                    self.phone,
                    self.ip
                )
            else:
                UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
                user_exists = UserProfile.objects.filter(email=self.cleaned_data.get("email")).exists()
                if not user_exists:
                    self.create_user(
                        self.cleaned_data.get("email"), 
                        self.cleaned_data.get("password"),
                        self.cleaned_data.get("country"),
                        self.cleaned_data.get("firstName"),
                        self.cleaned_data.get("lastName"),
                        self.phone,
                        self.ip,
                        False
                    )
        except:
            UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
            user_exists = UserProfile.objects.filter(email=self.cleaned_data.get("email")).exists()
            if not user_exists:
                self.create_user(
                    self.cleaned_data.get("email"), 
                    self.cleaned_data.get("password"),
                    self.cleaned_data.get("country"),
                    self.cleaned_data.get("firstName"),
                    self.cleaned_data.get("lastName"),
                    self.phone,
                    self.ip,
                    False
                )
        try:
            login_url = json_data["data"]["loginToken"]
        except:
            login_url = None
        return True, login_url

    def get_customers(self, token):
        url = 'https://mena-evest.pandats-api.io/api/v3/customers'

        authorization = 'Bearer %s' %token

        headers = {
            'Content-Type': 'application/json',
            'Authorization': authorization
        }

        # data = {
        #     'email': 'aaa@gmail.com'
        # }

        # data_json = simplejson.dumps(data)

        r = requests.get(url, headers=headers)

        json_data = json.loads(r.content.decode('utf-8'))

    def create_user(self, email, password, country, firstName, lastName, phone, ip=None, registered=True):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug,
            ip=ip,
            registered=registered
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="evest")
            api_reg_type_obj.members.add(user)
        except:
            pass



# ─── TRADE 360 FORM ─────────────────────────────────────────────────────────────────
class Trade360Form(forms.Form):
    firstName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    def post_customer(self):        
        url = 'https://server.paragonex-network.com/api/v1/signups/add.php'
        api_key = "5B2E3DDF-A4B4-2435-F00B-1EB39C07D95D"

        token_header = 'Api-Key: %s' %api_key

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Api-Key': api_key
        }

        data = {
            'email': self.cleaned_data.get("email"),
            'password': self.cleaned_data.get("password"),
            'firstName': self.cleaned_data.get("firstName"),
            'lastName': self.cleaned_data.get("lastName"),
            'phone': self.cleaned_data.get("phone"),
            "ip": "167.172.41.255",
            "isTest": 1,
            "locale": "en-GB",
            "offerName": "test-offer",
            "offerWebsite": "https://economyflow.com",
            "comment": "test comment"
        }

        data_json = simplejson.dumps(data)


        r = requests.post(url, headers=headers, data=data_json)
        json_data = json.loads(r.content.decode('utf-8'))
        
        # try:
        #     status = json_data["data"]["status"]
        #     if status == "ok":
        #         self.create_user(
        #             self.cleaned_data.get("email"), 
        #             self.cleaned_data.get("password"),
        #             self.cleaned_data.get("firstName"),
        #             self.cleaned_data.get("lastName"),
        #             self.cleaned_data.get("phone")
        #         )
        # except:
        #     pass

    def create_user(self, email, password, firstName, lastName, phone):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            firstName=firstName,
            lastName=lastName
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="Trade360")
            
            api_reg_type_obj.members.add(user)
        except:
            pass


# ─── EVEST FORM ─────────────────────────────────────────────────────────────────
class LegacyFxForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page_slug = kwargs.pop("page_slug")
        self.tag = kwargs.pop("tag")
        super().__init__(*args, **kwargs)
    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    firstName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    country = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    def get_api_key(self):
        url = 'https://affiliate.legacyfx.com/api/affiliate/generateauthtoken'

        data = {
            'userName': 'Mokhbir Eqtisadi',
            'password': "U5sd6@sQ"
        }

        data_json = simplejson.dumps(data)


        headers = {
            'Content-Type': 'application/json',
        }

        r = requests.post(url, headers=headers, data=data_json)

        

        json_data = json.loads(r.content.decode('utf-8'))

        token = json_data['token']
        return token

    def post_customer(self):
        token = self.get_api_key()

        
        
        url = 'https://affiliate.legacyfx.com/api/aff/accounts'

        headers = {
            'Content-Type': 'application/json',
            'AuthToken': token
        }

        data = {
            'Email': self.cleaned_data.get("email"),
            'Country': self.cleaned_data.get("country"),
            'FirstName': self.cleaned_data.get("firstName"),
            'LastName': self.cleaned_data.get("lastName"),
            'Phone': self.cleaned_data.get("phone"),
            "AffiliateId": "36396", #36279-bash
            "Tag": self.tag, #"ashraf_channel",
            "Tag1": self.tag, #"ashraf_channel",
            "SiteLogin": "/single-page#/deposit-methods",
            "IsDemo": False,
            "AcceptTerms": True,
            "WTLogin": True
        }

        data_json = simplejson.dumps(data)

        r = requests.post(url, headers=headers, data=data_json)
        json_data = json.loads(r.content.decode('utf-8'))

        self.create_user(
            self.cleaned_data.get("email"), 
            self.cleaned_data.get("country"),
            self.cleaned_data.get("firstName"),
            self.cleaned_data.get("lastName"),
            self.cleaned_data.get("phone"),
        )

        if json_data["SiteLoginUrl"]:
            return json_data["SiteLoginUrl"]
        else:
            return None

    def create_user(self, email, country, firstName, lastName, phone):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="legacyfx")
            api_reg_type_obj.members.add(user)
        except:
            pass



class IngotForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page_slug = kwargs.pop("page_slug")
        super().__init__(*args, **kwargs)
    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    firstName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    country = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    phone = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    post_code = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    def post_customer(self): 
        url = "https://www.ingotbrokers.com/api/v1/ingot/create-application"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "svsRMxz8AleGJW2ILXna7kJPhqLaEfT33PwtCPfYqLIgTluunkiKvX8TNd5DZ3FX"
        }

        mod_phone = self.cleaned_data.get("phone")
        if mod_phone[0] == "+":
            mod_phone = mod_phone[1:]
        elif mod_phone[0] == "0":
            mod_phone = mod_phone[1:]

        data = {
            'email': self.cleaned_data.get("email"),
            'password': self.cleaned_data.get("password"),
            'country': self.cleaned_data.get("country"),
            'first_name': self.cleaned_data.get("firstName"),
            'last_name': self.cleaned_data.get("lastName"),
            'phone': mod_phone,
            'post_code': self.cleaned_data.get("post_code"),
            'token': '048f383950a721ed75bed9fe6eb16af1'
        }

        data_json = simplejson.dumps(data)

        r = requests.post(url, headers=headers, data=data_json)


        json_data = json.loads(r.content.decode('utf-8'))

        self.create_user(
            self.cleaned_data.get("email"), 
            self.cleaned_data.get("password"),
            self.cleaned_data.get("country"),
            self.cleaned_data.get("firstName"),
            self.cleaned_data.get("lastName"),
            self.cleaned_data.get("phone"),
        )

        if json_data["success"] == True:
            return True
        else:
            return False

    def create_user(self, email, password, country, firstName, lastName, phone):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="ingot")
            api_reg_type_obj.members.add(user)
        except:
            pass


class AlvexoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page_slug = kwargs.pop("page_slug")
        super().__init__(*args, **kwargs)

    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    fullName = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    telephone = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    countryID = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    clientIP = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))

    def post_customer(self):        
        url = "https://trader.alvexo.com/web-api/v3/lead/register-aff?bn_cmp=2757470&t_cre=start-campaign&bn_source=economyflow"
        token = "fwqass2rfa=2rNDMzOWFzY29pMW5iczIyZmVhc3ZlMzVlYXNkZmFsdmV4bw=="
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        password = "Nstu1234!@"
        demolive = 2
        language = "ar"
        lpID = 2832

        telephone = self.cleaned_data.get("telephone")
        phone_code = phone_codes.get(self.cleaned_data.get("countryID"))
        
        if telephone[0] == "0":
            telephone = telephone[1:len(telephone)]

        if phone_code in telephone:
            pass
        else:
            telephone = phone_code + telephone

        data = {
            'inputs[email]': self.cleaned_data.get("email"),
            'inputs[fullName]': self.cleaned_data.get("fullName"),
            'inputs[telephone]': telephone,
            'inputs[password]': password,
            'inputs[demolive]': demolive,
            'inputs[countryID]': self.cleaned_data.get("countryID"),
            'inputs[clientIP]': self.cleaned_data.get("clientIP"),
            'inputs[token]': token,
            'inputs[lpID]': lpID,
            'inputs[clientUseragent]': user_agent,
            'inputs[language]': language
        }

        r = requests.post(url, headers=headers, data=data)
        json_data = json.loads(r.content.decode('utf-8'))
        
        try:
            status = json_data["succeeded"]
            if status == True:
                self.create_user(
                    self.cleaned_data.get("email"), 
                    self.cleaned_data.get("password"),
                    self.cleaned_data.get("countryID"),
                    self.cleaned_data.get("fullName"),
                    self.cleaned_data.get("fullName"),
                    self.cleaned_data.get("telephone")
                )
        except:
            pass
        try:
            login_url = json_data["url"]
        except:
            login_url = None
        return login_url

    def create_user(self, email, password, country, firstName, lastName, phone):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="alvexo")
            api_reg_type_obj.members.add(user)
        except:
            pass



class TradersGCCForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page_slug = kwargs.pop("page_slug")
        super().__init__(*args, **kwargs)

    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    full_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    phone = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    countryID = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    clientIP = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Country'}))

    def post_customer(self):        
        url = "https://platform.revotracking.com/api/signup/procform"
        token = "2643889w34df345676ssdas323tgc738"
        headers = {
            "Content-Type": "application/json",
            "x-trackbox-username": "Economyflow",
            "x-trackbox-password": "Economyflow2806",
            "x-api-key": token,
        }
        password = "Aa12345"
        split_full_name = self.cleaned_data.get("full_name").split(" ")
        firstname = split_full_name[0]
        lastname = split_full_name[1]

        phone = self.cleaned_data.get("phone")
        parse_number = phonenumbers.parse(phone, self.cleaned_data.get("countryID"))
        number_is_valid = phonenumbers.is_valid_number(parse_number)
        if number_is_valid:
            format_number = phonenumbers.format_number(parse_number, phonenumbers.PhoneNumberFormat.E164)

            data = {
                "ai": "2958269",
                "ci": "9",
                "gi": "221",
                "userip": self.cleaned_data.get("clientIP"), #"118.179.134.11"
                "firstname": firstname,
                "lastname": lastname,
                "email": self.cleaned_data.get("email"),
                # "password": password,
                "phone": format_number,
                "so": "AFF_2958269",
                "MPC_4": "Economyflow",
            }
            data_json = simplejson.dumps(data)

            r = requests.post(url, headers=headers, data=data_json)
            json_data = json.loads(r.content.decode('utf-8'))

            return json_data
            
            try:
                status = json_data["status"]
                data = json_data["data"]
                if status == True:
                    self.create_user(
                        self.cleaned_data.get("email"), 
                        password,
                        self.cleaned_data.get("countryID"),
                        firstname,
                        lastname,
                        phone
                    )
                    return data
            except:
                pass
            return None
        else:
            raise forms.ValidationError("Phone number not correct!")

    def create_user(self, email, password, country, firstName, lastName, phone):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="axia")
            api_reg_type_obj.members.add(user)
        except:
            pass


class CapitalForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page_slug = kwargs.pop("page_slug")
        self.user_ip = kwargs.pop("user_ip")
        self.country_code = kwargs.pop("country_code")
        self.params = kwargs.pop("params")
        super().__init__(*args, **kwargs)

    username = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': 'Password'}))

    def post_customer(self):        
        url = "https://affiliates.backend-capital.com/affiliates/api/v1/register"

        us_pass = b"menareefat-api:wZuAXJvqQP8whOgCeG13"
        b64Val = base64.b64encode(us_pass).decode('utf-8')

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {b64Val}"
        }

        print("+++++++")
        print(headers)

        data = {
            "username": self.cleaned_data.get("username"),
            "password": self.cleaned_data.get("password"),
            "country": self.country_code,
            "tenant": "CAPITAL_COM",
            "affId": "37051",
            "affTracking": self.params,
        }
        data_json = simplejson.dumps(data)
        print(data_json)

        r = requests.post(
            url, 
            headers=headers, 
            json=data
        )
        json_data = json.loads(r.content.decode('utf-8'))
        print("===========")
        print(r)
        print(json_data)

        if json_data:
            if json_data.get("authCode", None):
                auth_code = json_data["authCode"]
                userId = json_data["userId"]
                red_url = f"https://capital.com/trading/signup?&t={auth_code}&ln=ar&go=signup"

                UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
                ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')
                user = UserProfile.objects.create(
                    email=self.cleaned_data.get("username"),
                    country=self.country_code,
                    ip=self.user_ip,
                    campaign=self.page_slug,
                    registered=True,
                    sign_up_id=userId
                )
                try:
                    api_reg_type_obj = ApiRegistration.objects.get(type="capital")
                    api_reg_type_obj.members.add(user)
                except:
                    pass

                return red_url

        # return json_data
            
        # try:
        #     status = json_data["status"]
        #     data = json_data["data"]
        #     if status == True:
        #         self.create_user(
        #             self.cleaned_data.get("email"), 
        #             password,
        #             self.cleaned_data.get("countryID"),
        #             firstname,
        #             lastname,
        #             phone
        #         )
        #         return data
        # except:
        #     pass
        return None

    def create_user(self, email, password, country, firstName, lastName, phone):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="axia")
            api_reg_type_obj.members.add(user)
        except:
            pass


class AvaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.page_slug = kwargs.pop("page_slug")
        self.user_ip = kwargs.pop("user_ip")
        self.country_code = kwargs.pop("country_code")
        self.params = kwargs.pop("params")
        super().__init__(*args, **kwargs)

    email = forms.EmailField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    telephone = forms.CharField(max_length=50, required=True)

    def clean(self):
        phone = self.cleaned_data.get("telephone")
        parse_number = phonenumbers.parse(phone, self.country_code)
        number_is_valid = phonenumbers.is_valid_number(parse_number)
        if not number_is_valid:
            raise forms.ValidationError({"telephone": ["Phone number not correct!",]})
        return self.cleaned_data

    def post_customer(self):        
        url = "https://api.avaapi.net/api/aows/register/v3/real"

        headers = {
            "Content-Type": "application/json",
            "api_key": "BtYOPDFCLUy5uvxtm3PXLw"
        }

        phone = self.cleaned_data.get("telephone")
        parse_number = phonenumbers.parse(phone, self.country_code)
        number_is_valid = phonenumbers.is_valid_number(parse_number)
        if number_is_valid:
            format_number = phonenumbers.format_number(parse_number, phonenumbers.PhoneNumberFormat.E164)

            data = {
                "email": self.cleaned_data.get("email"),
                "first_name": self.cleaned_data.get("first_name"),
                "last_name": self.cleaned_data.get("last_name"),
                "country": self.country_code,
                "affiliate_id": "173016",
                "ip_address": self.user_ip,
                "Telephone": format_number,
                "tag2": self.params
            }
            # data_json = simplejson.dumps(data)
            # print(data_json)

            r = requests.post(
                url, 
                headers=headers, 
                json=data
            )
            json_data = json.loads(r.content.decode('utf-8'))
            try:
                red_url = json_data["MyAvaRedirectUrl"]
                self.create_user(
                        self.cleaned_data.get("email"), 
                        self.country_code,
                        self.cleaned_data.get("first_name"),
                        self.cleaned_data.get("last_name"),
                        format_number,
                        self.user_ip
                    )
                return False, red_url
            except:
                return True, json_data.get("error", None)
        else:
            raise forms.ValidationError("Phone number not correct!")

    def create_user(self, email, country, firstName, lastName, phone, ip):
        UserProfile = apps.get_model(app_label='home', model_name='UserProfile')
        ApiRegistration = apps.get_model(app_label='home', model_name='ApiRegistration')

        user = UserProfile.objects.create(
            email=email,
            phone=phone,
            country=country,
            firstName=firstName,
            lastName=lastName,
            campaign=self.page_slug,
            ip=self.user_ip
        )
        try:
            api_reg_type_obj = ApiRegistration.objects.get(type="ava")
            api_reg_type_obj.members.add(user)
        except:
            pass