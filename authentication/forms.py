# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Phone Number",                
                "class": "form-control"
            }
        ))
    addressline1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line1",                
                "class": "form-control"
            }
        ))
    addressline2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line2",                
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        ))
    pincode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Pincode",                
                "class": "form-control"
            }
        ))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'addressline1', 'addressline2', 'city', 'pincode')
