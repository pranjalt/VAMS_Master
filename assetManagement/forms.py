#from django import generic
from django import forms
from material import *
from .models import *
from sportsList.models import *

from cProfile import label
from sportsList.models import *
from crispy_forms.layout import *
from crispy_forms.helper import FormHelper

""""  
class AssetManagementForm(forms.ModelForm):
	#asset_mg_id = forms.IntegerField(required=False,label="First Name")
    vendor = forms.ModelChoiceField(queryset=Vendor.objects.all(),required=True)
    asset = forms.ModelChoiceField(queryset=Asset.objects.all(),required=True,label="Asset")
    sports = forms.ModelChoiceField(queryset=Sports.objects.all(),required=True,label="Sport")
    school = forms.ModelChoiceField(queryset=School.objects.all(),required=True)
    max_quantity = forms.IntegerField(required=False,label="Maximum assets")
    quantity_left = forms.IntegerField(required=True,label="required_quantity" )
    issue_date = forms.DateTimeField(required=False, label="Asset issue date" )
    return_date = forms.DateTimeField(required=False,label="Asset return date" )
	
   
    class Meta:
        model = Vendor
        fields = ('max_quantity', 'quantity_left')
        model = Assetmanagement
        fields = ('vendor', 'asset','sports','school','max_quantity','quantity_left','issue_date','return_date') 
"""	

