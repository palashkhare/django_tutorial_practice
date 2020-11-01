from django import forms
from login_app import models
from django.contrib.auth.models import User

# -*- coding: utf-8 -*-

class contact_me_form(forms.ModelForm):
    class Meta():
        model = models.contact_me
        fields = '__all__'
        

# Create a form for User database
class UserProfileForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        
class UserProfileExtention(forms.ModelForm):
    class Meta():
        model = models.UserProfileExtention
        fields = ('portfolio_site', 'picture')