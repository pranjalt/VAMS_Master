#from django import generic
from django import forms
#from material import *
from .models import *
from cProfile import label
from models import Onboarding
from sportsList.models import *
from crispy_forms.layout import *
from crispy_forms.helper import FormHelper
    
class OnBoardingForm(forms.ModelForm):
    def _init_(self, *args,**kwrgs):
        super(OnBoardingForm,self)._init_(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_id = 'id-OnBoardingForm'
		
    first_name = forms.CharField(max_length=50,required=False,label="First Name")
    middle_name=forms.CharField(max_length=50,required=False,label="Middle Name")
    last_name=forms.CharField(max_length=50,required=False,label="Last Name")
    #gender = forms.ChoiceField(queryset=Gender.objects.all(),widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    email_id=forms.CharField(max_length=100,required=False,label="Email Id")
    sports=forms.ModelChoiceField(queryset=Sports.objects.all(),label="Sport",widget = forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    #sports=forms.ChoiceField(choices=list(Sports.objects.all()))
    total_yrs_exp=forms.IntegerField(required=False)
    sec_ques1=forms.ModelChoiceField(queryset=SecurityQuestions.objects.all(),label="Security question2",widget=forms.Select(attrs={'placeholder':'Security_Qes'}))
    sec_ans1=forms.CharField(max_length=100,required=False)
    sec_ques2=forms.ModelChoiceField(queryset=SecurityQuestions.objects.all(),label="Security question2")
    sec_ans2=forms.CharField(max_length=100,required=False)

    address = forms.IntegerField(required=False)
    country=forms.ModelChoiceField(queryset=Country.objects.all(),required=False,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    province=forms.ModelChoiceField(queryset=Province.objects.all(),required=False,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    city=forms.ModelChoiceField(queryset=City.objects.all(),required=False,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))
    street1=forms.CharField(max_length=30,required=False, help_text="Enter Street1")
    street2=forms.CharField(max_length=30,required=False, help_text="Enter Street2")
    zipcode=forms.IntegerField(required=False,help_text="Enter Zipcode")
    role = forms.ModelChoiceField(queryset=Role.objects.all(),required=False,label="Enter Role" ,widget=forms.Select(attrs={'class' :'reg-form-dropdown-border'}))

   
    layout = Layout(Row('first_name','middle_name','last_name'),
                    Row('email_id')
                    )
	
    class Meta:
        model = Address
        fields = ('country', 'province','city','street1','street2','zipcode')
        model = Onboarding
        fields = ('first_name', 'middle_name','last_name','email_id','sports','total_yrs_exp','sec_ques1','sec_ans1','sec_ques1','sec_ans2','address','role')
	
