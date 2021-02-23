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


# --------------------------Customer related----------------------------
class CustomerForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name",                
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password1",                
                "class": "form-control"
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password2",                
                "class": "form-control"
            }
        ))
    
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
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
    # is_staff = forms.BooleanField(initial=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'addressline1', 'addressline2', 'city', 'pincode', 'is_active']
        exclude = ['user', 'groups', 'user_permissions', 'is_superuser', 'last_login', 'is_staff', 'date_joined']

Customerformset = inlineformset_factory(User, Customer, 
    fields=('Account_Number', 'STB_Number', 'Area_Name', 'NODE_Number', 'Bank_Account', 'IFSC_code', 'is_active'), extra=1, 
    can_delete=False) 


# --------------------------Operator related-----------------------------------------
class OperatorForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name",                
                "class": "form-control",
            }
        ))

    
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
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
    
    is_staff = forms.BooleanField(initial=True)
    is_active = forms.BooleanField(initial=True)

    password1 = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password1",                
                "class": "form-control"
                
                
            }
        ))
    password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password2",                
                "class": "form-control"
                
                
            }
        ))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',  'phone', 'addressline1', 'addressline2', 'city', 'pincode', 'is_active', 'is_staff' ]
       

Operatorformset = inlineformset_factory(User, Operator, 
    fields=('Area', 'Pan_Number', 'Bank_Account', 'IFSC_code'), extra=1, 
    can_delete=False) 



class CreatePlansForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Plan Name",                
                "class": "form-control"
            }
        ))
    
    plan_ID = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Plan ID",                
                "class": "form-control"
            }
        ))
    
    validity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Validity",                
                "class": "form-control"
            }
        ))

    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Price ₹",                
                "class": "form-control"
            }
        ))

    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Company Name",                
                "class": "form-control"
            }
        ))

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Description",                
                "class": "form-control"
            }
        ))

    speed = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Speed Line",                
                "class": "form-control"
            }
        ))

    data_limit = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Data Limit",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Plans
        fields = '__all__'


class EmployeeForm(ModelForm):
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address",                
                "class": "form-control"
            }
        ))

    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Name",                
                "class": "form-control"
            }
        ))

    Emp_Number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee Number",                
                "class": "form-control"
            }
        ))

    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile",                
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email Address",                
                "class": "form-control"
            }
        ))

    department = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Department",                
                "class": "form-control"
            }
        ))

    DOJ = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "DD-MM-YYYY",                
                "class": "form-control datepicker"
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

    company_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Company Name",                
                "class": "form-control"
            }
        ))

    bank_account_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Bank Account Number",                
                "class": "form-control"
            }
        ))

    ifsc_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "IFSC COde",                
                "class": "form-control"
            }
        ))

    branch_addresss = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Branch Address",                
                "class": "form-control"
            }
        ))

    branch_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Branch Name",                
                "class": "form-control"
            }
        ))

    permission = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Permission",                
                "class": "form-control"
            }
        ))
    class Meta:
        model = Employee
        fields = '__all__'

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class stbForm(forms.ModelForm):
    serial_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "label" : "Serial Number",
                "placeholder" : "Serial Number",                
                "class": "form-control"
            }
        ))
    issue_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "label" : "Issue Date",               
                "class": "form-control datepicker"
            }
        ))
    
    
    DOP = forms.DateField(
        widget=forms.DateInput(
            attrs={              
                "class": "form-control datepicker "
            }
        ))
    
    remark = forms.CharField(
        widget=forms.Textarea(
            attrs={    
                "placeholder" : "Remark",            
                "class": "form-control "
            }
        ))
    model_number = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "placeholder" : "Model Number",            
                "class": "form-control "
            }
        ))  
    Type = forms.ChoiceField(
        choices=Type_choices,
        widget=forms.Select(
            attrs={    
                "label" : "Type",            
                "class": "form-control "
            }
        ))
    box_type = forms.ChoiceField(
        choices=Box_choices,
        widget=forms.Select(
            attrs={    
                "label" : "Type",            
                "class": "form-control "
            }
        ))
    status = forms.ChoiceField(
        choices=Status_choices,
        widget=forms.Select(
            attrs={    
                "label" : "status",            
                "class": "form-control "
            }
        ))
    
    class Meta:
        model = STB
        fields = '__all__'
        exclude= ('user_id', 'is_assigned')
    
class nodeForm(forms.ModelForm):
    serial_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "label" : "Serial Number",
                "placeholder" : "Serial Number",                
                "class": "form-control"
            }
        ))
    issue_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "label" : "Issue Date",               
                "class": "form-control datepicker"
            }
        ))
    
    
    DOP = forms.DateField(
        widget=forms.DateInput(
            attrs={              
                "class": "form-control datepicker "
            }
        ))
    
    remark = forms.CharField(
        widget=forms.Textarea(
            attrs={    
                "placeholder" : "Remark",            
                "class": "form-control "
            }
        ))
    model_number = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "placeholder" : "Model Number",            
                "class": "form-control "
            }
        ))  
    STB_count = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "label" : "STB_count",
                "placeholder" : "STB Count",       
                "class": "form-control"
            }
        ))
    area = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "label" : "Area",
                "placeholder" : "Area",        
                "class": "form-control "
            }
        ))
    status = forms.ChoiceField(
        choices=Status_choices,
        widget=forms.Select(
            attrs={    
                "label" : "status",            
                "class": "form-control "
            }
        ))
    
    class Meta:
        model = Node
        fields = '__all__'

class routerForm(forms.ModelForm):
    make = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "label" : "Make",
                "placeholder" : "Make",                
                "class": "form-control"
            }
        ))
    issue_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "label" : "Issue Date",               
                "class": "form-control datepicker"
            }
        ))
    
    
    DOP = forms.DateField(
        widget=forms.DateInput(
            attrs={              
                "class": "form-control datepicker "
            }
        ))
    
    remark = forms.CharField(
        widget=forms.Textarea(
            attrs={    
                "placeholder" : "Remark",            
                "class": "form-control "
            }
        ))
    model_number = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "placeholder" : "Model Number",            
                "class": "form-control "
            }
        ))  
    mac_id = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "label" : "mac_id",
                "placeholder" : "MAC ID",       
                "class": "form-control"
            }
        ))
    ip_address = forms.GenericIPAddressField(
        widget=forms.TextInput(
            attrs={    
                "label" : "ip_address",
                "placeholder" : "IP Address",        
                "class": "form-control "
            }
        ))
    status = forms.ChoiceField(
        choices=Status_choices,
        widget=forms.Select(
            attrs={    
                "label" : "status",            
                "class": "form-control "
            }
        ))
    type1 = forms.ChoiceField(
        choices=type1_choices,
        widget=forms.Select(
            attrs={    
                "label" : "type1",            
                "class": "form-control "
            }
        ))
    router_type = forms.ChoiceField(
        choices=router_Choices,
        widget=forms.Select(
            attrs={    
                "label" : "router_type",            
                "class": "form-control "
            }
        ))
    
    class Meta:
        model = Router
        fields = '__all__'


class InventoryForm(forms.ModelForm):
    item_name = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "label" : "item_name",
                "placeholder" : "Item Name",       
                "class": "form-control"
            }
        ))
    vendor_name = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "label" : "vendor_name",
                "placeholder" : "Vendor's Name",       
                "class": "form-control"
            }
        ))
    receiver_name = forms.CharField(
        widget=forms.TextInput(
            attrs={    
                "label" : "receiver_name",
                "placeholder" : "Receiver's Name",       
                "class": "form-control"
            }
        ))
    qty = forms.CharField(
        widget=forms.NumberInput(
            attrs={    
                "label" : "qty",
                "placeholder" : "Quantity",       
                "class": "form-control"
            }
        ))
    amount = forms.CharField(
        widget=forms.NumberInput(
            attrs={    
                "label" : "amount",
                "placeholder" : "Amount",       
                "class": "form-control"
            }
        ))
    bill_number = forms.CharField(
        widget=forms.NumberInput(
            attrs={    
                "label" : "bill_number",
                "placeholder" : "Bill Number",       
                "class": "form-control"
            }
        ))
    
    date_of_purchase = forms.DateField(
        widget=forms.DateInput(
            attrs={              
                "class": "form-control datepicker "
            }
        ))

    warehouse = forms.ChoiceField(
        choices=warehouse_choices,
        widget=forms.Select(
            attrs={    
                "label" : "Warehouse",            
                "class": "form-control "
            }
        ))
    class Meta:
        model = Inventory
        fields = '__all__'