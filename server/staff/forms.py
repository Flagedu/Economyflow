from django import forms
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User


# ─── LOGIN FORM ─────────────────────────────────────────────────────────────────
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'User ID'}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 1:
            raise forms.ValidationError('Enter User ID!')
        else:
            if len(password) < 8:
                raise forms.ValidationError('Password is too short!')
            else:
                user = authenticate(self, username=username, password=password)

                if not user:
                    raise forms.ValidationError('Email or Password not matched!')
                else:
                    if user.is_staff or user.is_superuser:
                        pass
                    else:
                        raise forms.ValidationError('You dont have enough permission to login!')

                    if not user.is_active:
                        raise forms.ValidationError('Account blocked! Please contact customer support!')


    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(self, username=username, password=password)
        return user