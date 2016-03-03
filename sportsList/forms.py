from django import forms
from material import *
from .models import *
from cProfile import label
from crispy_forms.layout import Layout,Row

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")
  

    
class AddressForm(forms.ModelForm):
    country=forms.ModelChoiceField(queryset=Country.objects.all(),required=False,help_text="Select Country")
    province=forms.ModelChoiceField(queryset=Province.objects.all(),required=False,help_text="Select Province")
    city=forms.ModelChoiceField(queryset=City.objects.all(),required=False,help_text="Select City")
    street1=forms.CharField(max_length=30,required=False, help_text="Enter Street1")
    street2=forms.CharField(max_length=30,required=False, help_text="Enter Street2")
    zipcode=forms.IntegerField(required=False,help_text="Enter Zipcode")
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Address
        fields = ('country', 'province','city','street1','street2','zipcode')



class OnBoardingForm(forms.ModelForm):

    first_name = forms.CharField(max_length=50,required=False,label="First Name")
    middle_name=forms.CharField(max_length=50,required=False,label="Middle Name")
    last_name=forms.CharField(max_length=50,required=False,label="Last Name")
    #gender = forms.ChoiceField(queryset=Gender.objects.all(),widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    email_id=forms.CharField(max_length=100,required=False,label="Email Id")
    contact_no=models.IntegerField(max_length=10,help_text="Enter Contact No")
    sports=forms.ModelChoiceField(queryset=Sports.objects.all(),label="Sport", widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
   # sports=forms.ChoiceField(choices=list(Sports.objects.all()))
    total_yrs_exp=forms.IntegerField(required=False)
    sec_ques1=forms.ModelChoiceField(queryset=SecurityQuestions.objects.all(),label="Security question 1", widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    sec_ans1=forms.CharField(max_length=100,required=False)
    sec_ques2=forms.ModelChoiceField(queryset=SecurityQuestions.objects.all(),required=False,label="Security question2", widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    sec_ans2=forms.CharField(max_length=100,required=False)
    address = forms.ModelChoiceField(queryset=Address.objects.all(),required=False)    
    country=forms.ModelChoiceField(queryset=Country.objects.all(),required=False,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    province=forms.ModelChoiceField(queryset=Province.objects.all(),required=False,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    city=forms.ModelChoiceField(queryset=City.objects.all(),required=False,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    street1=forms.CharField(max_length=30,required=False, help_text="Enter Street1")
    street2=forms.CharField(max_length=30,required=False, help_text="Enter Street2")
    zipcode=forms.IntegerField(required=False,help_text="Enter Zipcode")    
    role = forms.ModelChoiceField(queryset=Role.objects.all(),required=False,label="Enter Role" ,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))

    print SecurityQuestions.objects.all()
    print address
    layout = Layout(Row('first_name','middle_name','last_name'),
                    Row('email_id'),
                    Row('sports','total_yrs_exp'),
                    Row('sec_ques1','sec_ans1'),
                    Row('sec_ques2','sec_ans2'),
                    Row('country','province','city'),
                    Row('street1','street2','zipcode'),
                    'role'
                    )

