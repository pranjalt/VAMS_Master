from django import forms
from registerApp.models import Register

class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text="Enter Name.")
    address = forms.CharField(max_length=50,help_text="Enter Address.")
    
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Register
        fields = ('name', 'address')
