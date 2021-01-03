from django import forms
from django.contrib.auth.models import User
from models.py import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widgets=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('profile_pic')
