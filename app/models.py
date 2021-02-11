# -*- encoding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Operator(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Area = models.CharField(max_length=200, null=True)
    Pan_Number = models.CharField(max_length=20, null=True)
    Bank_Account = models.CharField(max_length=20, null=True)
    IFSC_code = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=1)
    is_staff = models.BooleanField(default=1)

    def __str__(self):
        return f'{self.user}'
    
class Customer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='customer')

    Account_Number = models.CharField(max_length=20, null=True)
    STB_Number = models.CharField(max_length=20, null=True)
    Area_Name = models.CharField(max_length=100, null=True)
    NODE_Number = models.CharField(max_length=20, null=True)
    Bank_Account = models.CharField(max_length=20, null=True)
    IFSC_code = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=1)

    USERNAME_FIELD= ('user')

    def __str__(self):
        return f'{self.user}'
