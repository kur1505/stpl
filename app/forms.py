from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction
from django.forms import inlineformset_factory
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *
from authentication.models import *
from authentication.forms import SignUpForm

class CustomerForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password','user', 'groups', 'user_permissions', 'is_superuser', 'last_login', 'is_staff', 'date_joined']

Customerformset = inlineformset_factory(User, Customer, 
    fields=('Account_Number', 'STB_Number', 'Area_Name', 'NODE_Number', 'Bank_Account', 'IFSC_code'), extra=1, 
    can_delete=False) 

# class CustomerForm2(UserCreationForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         exclude = ['password', 'groups', 'user_permissions', 'is_superuser', 'last_login', 'is_staff', 'date_joined']

        
