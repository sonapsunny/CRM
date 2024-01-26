from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Record
from django import forms
from django.contrib.auth.forms import AuthenticationForm


# create record 

class CreateRecordForm(forms.ModelForm):
    
    class Meta:

        model= Record
        fields=['first_name','last_name','email','phone','address','city','province','country','zipcode']


# update record

class UpdateRecordForm(forms.ModelForm):
    
    class Meta:

        model= Record
        fields=['first_name','last_name','email','phone','address','city','province','country','zipcode']

class EmailForm(forms.Form):
    to=forms.EmailField()
    sub=forms.CharField(max_length=50)
    cont=forms.CharField(max_length=300)