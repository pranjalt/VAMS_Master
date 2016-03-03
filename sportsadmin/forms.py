from django import forms
#from material import *
from sportsList.models import *
#from cProfile import label
from django.forms.models import inlineformset_factory
from Carousel.models import *
from django.forms import fields

class loginForm(forms.Form):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

    

    
class AddressForm(forms.ModelForm):
    country=forms.ModelChoiceField(queryset=Country.objects.all(),required=False,help_text="Select Country",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    province=forms.ModelChoiceField(queryset=Province.objects.all(),required=False,help_text="Select Province",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    city=forms.ModelChoiceField(queryset=City.objects.all(),required=False,help_text="Select City",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    street1=forms.CharField(max_length=30,required=False, help_text="Street1",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Street1','maxlength':'30','required':'False'}))
    street2=forms.CharField(max_length=30,required=False, help_text=" Street2",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Street2','maxlength':'30','required':'False'}))
    zipcode=forms.IntegerField(required=False,help_text="Zipcode",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Zipcode','maxlength':'6','required':'False'}))
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Address
        fields = ('country', 'province','city','street1','street2','zipcode')


class PlayerOnBoardingForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','maxlength':'50','placeholder':'First Name','required':'False'}))
    middle_name=forms.CharField(label="Middle Name",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Middle Name','maxlength':'50','required':'False'}))
    last_name=forms.CharField(label="Last Name",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Last Name','maxlength':'50','required':'False'}))
    gender=forms.ModelChoiceField(queryset=Gender.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
	#gender=forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')),widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    date_of_birth = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 date','placeholder':'yyyy-mm-dd', 'type':'date','data-fv-date':'true','data-fv-date-format':'YYYY/MM/DD','data-fv-date-message':'The value is not a valid date'}))
    email_id=forms.CharField(label="Email Id",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Email ID','maxlength':'100','required':'False'}))
    contact_no=forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Contact No','maxlength':'12','required':'False'}))
    sports=forms.ModelChoiceField(queryset=Sports.objects.all(),required=False,label="Sport",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    total_yrs_exp=forms.IntegerField(required=False,label="Total Yrs Experiance",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Total Yrs Experiance','maxlength':'2','required':'False'}))
    sec_ques=forms.ModelChoiceField(required=False,queryset=SecurityQuestions.objects.all(),label="Security question 1",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    sec_ans1=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Sequrity Answer','maxlength':'100','required':'False'}))
    address = forms.IntegerField(required=False)
    acd_reg = forms.ModelChoiceField(queryset=AcademyOnboarding.objects.all(),required=False,label="Enter Academy" ,widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    

    class Meta:
       
        model = PlayerOnboarding
        fields = ('first_name', 'middle_name','last_name','gender','email_id','contact_no','date_of_birth','sports','total_yrs_exp','sec_ques','sec_ans1','address','acd_reg')

		
class CoachOnBoardingForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','maxlength':'50','placeholder':'First Name','required':'False'}))
    middle_name=forms.CharField(label="Middle Name",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Middle Name','maxlength':'50','required':'False'}))
    last_name=forms.CharField(label="Last Name",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Last Name','maxlength':'50','required':'False'}))
    gender=forms.ModelChoiceField(queryset=Gender.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
	#gender=forms.ChoiceField(choices=((None, ''), ('F', 'Female'), ('M', 'Male'), ('O', 'Other')),widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    date_of_birth = forms.DateField(required=False,widget=forms.DateInput(attrs={'class':'form-control col-sm-3 date','placeholder':'yyyy-mm-dd', 'type':'date','data-fv-date':'true','data-fv-date-format':'YYYY/MM/DD','data-fv-date-message':'The value is not a valid date'}))
    email_id=forms.CharField(label="Email Id",required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Email ID','maxlength':'100','required':'False'}))
    contact_no=forms.IntegerField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Contact No','maxlength':'12','required':'False'}))
    sports=forms.ModelChoiceField(required=False,queryset=Sports.objects.all(),label="Sport",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    total_yrs_exp=forms.IntegerField(required=False,label="Total Yrs Experiance",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Total Yrs Experiance','maxlength':'2','required':'False'}))
    sec_ques=forms.ModelChoiceField(required=False,queryset=SecurityQuestions.objects.all(),label="Security question 1",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    sec_ans1=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Sequrity Answer','maxlength':'100','required':'False'}))
    address = forms.IntegerField(required=False)
    acd_reg = forms.ModelChoiceField(queryset=AcademyOnboarding.objects.all(),required=False,label="Enter Academy" ,widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    

    class Meta:
        # Provide an association between the ModelForm and a model
        model = CoachOnboarding
        fields = ('first_name', 'middle_name','last_name','gender','date_of_birth','email_id','contact_no','sports','total_yrs_exp','sec_ques','sec_ans1','address','acd_reg')

		
		
class AcademyOnboardingForm(forms.ModelForm):
    acd_reg=forms.CharField( required = False,widget=forms.HiddenInput())
    name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Name','maxlength':'100','required':'False'})) 
    estd = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control col-sm-3 date','placeholder':'yyyy-mm-dd', 'type':'date','data-fv-date':'true','data-fv-date-format':'YYYY/MM/DD','data-fv-date-message':'The value is not a valid date'}))
    email_id=forms.CharField(label="Email Id",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Email Id','maxlength':'100','required':'False'}))
    contact_no=forms.IntegerField(help_text="Enter Contact No",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Contact No','maxlength':'12','required':'False'}))
    website = forms.CharField(label="Website",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Website','maxlength':'50','required':'False'}))
    address = forms.CharField( required = False,widget=forms.HiddenInput())
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = AcademyOnboarding
        fields = ('name', 'estd','website','contact_no', 'email_id')
		
class CarouselVideoForm(forms.ModelForm):   
    movie_url=forms.CharField(label="Movie url",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Movie url','maxlength':'255','required':'True'}))  
    width=forms.IntegerField(help_text="Width",label="Width",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Width','required':'False'}))
    height=forms.IntegerField(help_text="Height",label="Height",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Height','required':'False'}))
    auto_play = forms.BooleanField(required=False,label="Auto Play")
    auto_hide = forms.BooleanField(required=False,label="Auto Hide")
    fullscreen = forms.BooleanField(required=False,label="Fullscreen")
    loop=forms.BooleanField(required=False,label="Loop")
    bgcolor=forms.CharField(label="bgcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'000000','maxlength':'6','required':'False'}))
    textcolor=forms.CharField(initial="FFFFFF",label="textcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'FFFFFF','maxlength':'6','required':'False'}))
    seekbarcolor=forms.CharField(initial="13ABEC",label="seekbarcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'13ABEC','maxlength':'6','required':'False'}))
    seekbarbgcolor=forms.CharField(initial="333333",label="seekbarbgcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'333333','maxlength':'6','required':'False'}))
    loadingbarcolor=forms.CharField(initial="828282",label="loadingbarcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'828282','maxlength':'6','required':'False'}))
    buttonoutcolor=forms.CharField(initial="333333",label="buttonoutcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'333333','maxlength':'6','required':'False'}))
    buttonovercolor=forms.CharField(initial="000000",label="buttonovercolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'000000','maxlength':'6','required':'False'}))
    buttonhighlightcolor=forms.CharField(initial="FFFFFF",label="buttonhighlightcolor",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'FFFFFF','maxlength':'6','required':'False'}))
    sports=forms.ModelChoiceField(queryset=Sports.objects.all(),label="Sport",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    sports_subtype=forms.ModelChoiceField(queryset=SportsSubtype.objects.all(),label="Sports Subtype",widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
    
	
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Carousel_video_video
        fields = ( 'movie_url','width','height','auto_play','auto_hide','fullscreen','loop','bgcolor','textcolor','seekbarcolor','seekbarbgcolor','loadingbarcolor','buttonoutcolor','buttonovercolor','buttonhighlightcolor','sports','sports_subtype')

		
class CarouselPictureForm(forms.ModelForm):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    FLOAT_CHOICES = ((LEFT,("left")),
                     (RIGHT,("right")),
                     (CENTER,("center")),
                     )
    image=forms.FileField(required=False)
    url=forms.CharField(max_length=255,required=False,label="Image url",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Image url','maxlength':'255','required':'False'}))
    alt=forms.CharField(max_length=255,required=False,label="alt",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'alt','maxlength':'255','required':'False'}))
    longdesc=forms.CharField(max_length=255,required=False,label="Long Description",widget=forms.TextInput(attrs={'class':'form-control col-sm-3','placeholder':'Long Description','maxlength':'255','required':'False'}))
    float= forms.ChoiceField( choices =FLOAT_CHOICES ,required = False,widget=forms.Select(attrs={'class':'form-control col-sm-3'}))
	
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Carousel_Picture
        fields = ('image','url','alt','longdesc','float')
