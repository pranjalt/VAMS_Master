from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render ,render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django_tables2 import RequestConfig
from tables import PlayerOnboardingTable, SportsTable
from filters import PlayerOnboardingFilter, SportsFilter
from serializers import *
from models import *
from forms import OnBoardingForm, AddressForm
from rest_framework import viewsets
from sportsList.serializers import SportListSerializer
from itertools import chain
from django.contrib.admin.templatetags.admin_list import result_list
from django.core.context_processors import csrf
from rest_framework import permissions
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# Create your views here.
def login_form(request):
    #form = RegistrationForm()
    return render_to_response("UserLogin.html", RequestContext(request,{}))

	
	
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#gaurav code 
def player(request):
    
    f = OnboardingFilter(request.GET, queryset=Onboarding.objects.all())
    if request.method == "GET":
        list1=list()
    for obj in f:
        list1.append(obj)
    table=OnboardingTable(list1)
    RequestConfig(request,paginate={"per_page": 5}).configure(table)
    return render(request, 'login_admin/PlayersList.html', {'table': table,'filter': f},)

def login(request):
    #DO login and Authentication.
    #DO login and Authentication.
    print "inside login view"
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    print "user authenticated"
    print username
    print password
    print user
    if user is not None:
        if user.is_active:
            #login(request, user)
            sport_list = Sports.objects.annotate(reg_count=Count('onboarding'))
    
            return render(request,'login_admin/provienceHome.html',{'prov_sport_list':sport_list,'user':user})
        else:
            print "error"           
    else:
        print "error1"
    
    #return redirect('prv_home')
    
    #return redirect('prv_home')
    
def sports_list(request):
    
    """    
    sport_list = Sports.objects.annotate(reg_count=Count('onboarding'))
    f = SportsFilter(request.GET, queryset=sport_list)
    if request.method == "GET":
        list2=list()
        list3 = list()
    for obj in f:
        #countVal = str(obj.reg_count)
        #list3.append(countVal)
        #print "sfdsdfafsdfsdfsdfsdfsdfsdf"+countVal
        #list2.append(obj + countVal)
        list2.append(obj)
        
        
        #SportsTable.Count = obj.reg_count
        #list3.append(obj.reg_count)
    result_list = list(chain(list2,list3))
    for result in result_list :
        print result
    table=SportsTable(list2)
    #RequestConfig(request).configure(table)
    print table
    RequestConfig(request,paginate={"per_page": 5}).configure(table)
    return render(request, 'login_admin/sportsList.html', {'table': table,'filter': f},)
    """
    
    
    sport_list = Sports.objects.annotate(reg_count=Count('onboarding'))
    #f = SportsFilter(request.GET, queryset=sport_list)
    """if request.method == "GET":
        list2=list()
        list3=list()
    for obj in f:
        countVal = str(obj.reg_count)
       
        SportsTable.Count = obj.reg_count
        cnt =str(SportsTable.Count)
        list2.append(cnt)
        #list3.append(SportsTable.Count)
        
    table=SportsTable(list2)
    #print "test table sorts count "+table.Count
    #print "test table sorts count "+table.__getattribute__()
    
    RequestConfig(request,paginate={"per_page": 5}).configure(sport_list)"""
    html = ""
    for sport in sport_list:
        html += "%s :: %s <br/>" % (sport.sports_name, sport.reg_count)    
    return render(request, 'players/sportsListPlugin.html', {'sport_list': sport_list})

  
    

def provience_home(request):
    return render_to_response("login_admin/provienceHome.html", {})

def players_list(request):
    f = PlayerOnboardingFilter(request.GET, queryset=PlayerOnboarding.objects.all()) 
    print f
    if request.method == "GET":
        list1=list()
    for obj in f:
        list1.append(obj)
    table=PlayerOnboardingTable(list1)
    RequestConfig(request,paginate={"per_page": 5}).configure(table)
    return render(request, 'sportListPlugin/PlayersList.html', {'table': table,'filter': f},)
    #return HttpResponse("I got the player list")
    

def registration_form(request):
    form = OnBoardingForm()
    c = {'form':form}
    c.update(csrf(request))
    return render_to_response("login_admin/Registration.html",c)


def submit_registration_form(request):
    return HttpResponse("form Submited")

#old one not in use
def registration(request):
    #return HttpResponse("Done")
    """
    form = OnBoardingForm()
    c = {'form':form}
    c.update(csrf(request))
    return render_to_response("login_admin/PlayersRegistration.html",c)
    """
    context = RequestContext(request)
    if request.method == 'POST':
        form = OnBoardingForm(request.POST)
        form1=AddressForm(request.POST)
        print 'abcdef'
        print form['first_name'].value()
        ffirst_name=form['first_name'].value()
        fmiddle_name=form['middle_name'].value()
        flast_name=form['last_name'].value()
        femail_id=form['email_id'].value()
        fcontact_no=form['contact_no'].value()
        fsports=form['sports'].value()
        print fsports
        ftotal_yrs_exp=form['total_yrs_exp'].value()
        fsec_ques1=form['sec_ques1'].value()
        fsec_ans1=form['sec_ans1'].value()
        fsec_ques2=form['sec_ques2'].value()
        fsec_ans2=form['sec_ans2'].value()
        frole=form['role'].value()       
        if form.is_valid():
            
            #Rohini changes
            key=form1.save()     
            form=Onboarding.objects.create(first_name=ffirst_name,middle_name=fmiddle_name,last_name=flast_name,email_id=femail_id,contact_no=fcontact_no,sports_id=fsports,total_yrs_exp=ftotal_yrs_exp,sec_ques_id=fsec_ques1,sec_ans1=fsec_ans1,sec_ans2=fsec_ans2,address_id=key.address_id,role_id=frole)
            form.save()
            print 'after saving form'
          
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = OnBoardingForm()
    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    form = OnBoardingForm()
    c = {'form':form}
    c.update(csrf(request))
    #sports_list()
    
    
#login code from gaurav
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def sport_list(request):
    return render_to_response(
    'sport_list.html',
    { 'user': request.user }
    )

class PlayerRegistration(viewsets.ModelViewSet):   
    queryset = PlayerOnboarding.objects.all()
    serializer_class = PlayerSerializer
   
   
   
class Country(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
    
class Province(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    
    
  
class Role(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
   
      
      
class City(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer    
    
    
class Gender(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    
    
class SecurityQuestions(viewsets.ModelViewSet):
    queryset = SecurityQuestions.objects.all()
    serializer_class = SecurityQuestionsSerializer
    
      
class PlayerListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PlayerListSerializer
    
    def get_queryset(self):
        queryset = PlayerOnboarding.objects.all()
        sports_name = self.request.query_params.get('sports_id', None)
        if sports_name is not None:
            queryset = queryset.filter(sports_id=sports_name).prefetch_related('sports')
        return queryset

class CoachRegistration(viewsets.ModelViewSet):
    #permission_classes = (permissions.AllowAny,permissions.DjangoModelPermissions,permissions.DjangoObjectPermissions,permissions.DjangoModelPermissionsOrAnonReadOnly,)
    serializer_class = CoachSerializer
    queryset = CoachOnboarding.objects.all()
    

class CoachList(viewsets.ModelViewSet):
    serializer_class = CoachListSerializer
    queryset = CoachOnboarding.objects.all() 
    pagination_class = StandardResultsSetPagination 	
    def get_queryset(self):
        queryset = CoachOnboarding.objects.all()
        coach_name = self.request.query_params.get('coach_id', None)
        if coach_name is not None:
            queryset = queryset.filter(coach_id=coach_name)
        return queryset 

class PlayerList(viewsets.ModelViewSet):
    serializer_class = PlayerListSerializer
    queryset = PlayerOnboarding.objects.all()  
    pagination_class = StandardResultsSetPagination 	
    def get_queryset(self):
        queryset = PlayerOnboarding.objects.all()
        player_name = self.request.query_params.get('player_id', None)
        if player_name is not None:
            queryset = queryset.filter(player_id=player_name)
        return queryset 

    
class PlayerLogin(viewsets.ModelViewSet):
    serializer_class = PlayerListSerializer
   # queryset = PlayerOnboarding.objects.all()   
    def get_queryset(self):
        queryset = PlayerOnboarding.objects.all()
        user_name = self.request.query_params.get('user_name', None)
        password = self.request.query_params.get('password', None)
        if user_name and password is not None:
            queryset = PlayerOnboarding.objects.filter(email_id=user_name,first_name=password)
        return queryset 
    
    
class CoachLogin(viewsets.ModelViewSet):
    serializer_class = CoachListSerializer
   # queryset = PlayerOnboarding.objects.all()   
    def get_queryset(self):
        queryset = CoachOnboarding.objects.all()
        user_name = self.request.query_params.get('user_name', None)
        password = self.request.query_params.get('password', None)
        if user_name and password is not None:
            queryset = CoachOnboarding.objects.filter(email_id=user_name,first_name=password)
        return queryset
    
   
class SportListViewSet(viewsets.ModelViewSet):
    queryset = Sports.objects.annotate(player_count = Count('playeronboarding'))
    serializer_class = SportListSerializer 
    
class Sports(viewsets.ModelViewSet):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer
    print 'Sports list fetched'  