from django.template.loader import render_to_string
from django.shortcuts import render ,render_to_response
from django.template import RequestContext
from sportsList.models import PlayerOnboarding,CoachOnboarding,AcademyOnboarding
from Carousel.models import *
from .tables import *
from .forms import *
from django.db.transaction import commit
from django.db import transaction
from django.template.loader import get_template, LoaderOrigin
from django.template import Context
from django.core import serializers
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import  requires_csrf_token
from django.shortcuts import render_to_response, render,redirect
from django.views.decorators.csrf import *
from .forms import *
from django.core.context_processors import csrf
from django.forms.models import model_to_dict
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

@login_required(login_url='/loginAdmin/')
def advanceSearch(request):
    return render(request, 'sportsadmin/advanceSearch.html')

def sportsAdminLogin(request):
    context = RequestContext(request)
    c = {'loginForm':loginForm}
    c.update(csrf(request))
    return render(request, 'sportsadmin/sportsAdminLogin.html',c)

def adminAuthenticate(request):
    context = RequestContext(request)
    c = {'loginForm':loginForm}
    c.update(csrf(request))
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
    # the password verified for the user
        if user.is_active:
            login(request, user)
            messages.success(request,"Welcome to the Academy System.");
            return render(request, 'sportsadmin/sportsadminpage.html')
        else:
            messages.error(request,"The password is valid, but the account has been disabled!");
    else:
    # the authentication system was unable to verify the username and password
        messages.error(request, "The username and password were incorrect.");
        return render(request, 'sportsadmin/sportsAdminLogin.html',c)

@login_required(login_url='/loginAdmin/')		
def adminLogout(request):
    logout(request)
    context = RequestContext(request)
    c = {'loginForm':loginForm}
    c.update(csrf(request))
    return render(request, 'sportsadmin/sportsAdminLogin.html',c)
   

def homePge(request):
	
    default_load_tab = ""
    
    try:
        default_load_tab = request.GET['default_load_tab']
        
    except:
        default_load_tab = ""
        
    return render_to_response("sportsadmin/sportsadminpage.html", {'default_load_tab':default_load_tab}, RequestContext(request,{}))
    #return render_to_response("sportsadmin/sportsadminpage.html", RequestContext(request,{}))
	
@login_required(login_url='/loginAdmin/')	
def VideoList(request):   
    context = RequestContext(request)
    videos=  Carousel_video_video.objects.all()   
    video = CarouselVideoTable(Carousel_video_video.objects.all()) 
    videoform=CarouselVideoForm()   
    c = {'VideoList':video,'videoform':videoform}
    c.update(csrf(request))
    return render_to_response("sportsadmin/VideoList.html",c)
	
@login_required(login_url='/loginAdmin/')	
def PictureList(request):
    
    context = RequestContext(request)
    pictures=  Carousel_Picture.objects.all()  
    picture = CarouselPictureTable(Carousel_Picture.objects.all()) 
    pictureform=CarouselPictureForm()   
   
    c = {'PictureList':picture,'pictureform':pictureform}
    c.update(csrf(request))
    return render_to_response("sportsadmin/PictureList.html",c)

@login_required(login_url='/loginAdmin/')
def PlayerList(request):
    print "start of PlayerList"
    context = RequestContext(request)
    qs=request.user.groups.values_list("name",flat=True)
    querySet=None
    querySet1=None
    player=None
    
    #Query to get coaches for particular Academy login
    if not qs:
	 # admin login
     player = PlayerTable(PlayerOnboarding.objects.all())
    elif qs[1] and qs[0]!="common":
      print "academy login"
     #academy login
      print qs[0]
      queryset=AcademyOnboarding.objects.filter(name=qs[0])
      print queryset
      player = PlayerTable(PlayerOnboarding.objects.filter(acd_reg=queryset[0].acd_reg_id))
      print player
    elif qs[0]=='common' and qs[1]:
     # province login
     print "province login"
     querySet=Province.objects.filter(province_name=qs[1])
     querySet1=Address.objects.filter(province=querySet[0].province_id)
     player = PlayerTable(PlayerOnboarding.objects.filter(address__in =querySet1))
    	 
    
   
    playerform=PlayerOnBoardingForm()
    addressform=AddressForm()
   
    c = {'PlayerList':player,'playerform':playerform,'addressform':addressform}
    c.update(csrf(request))
    return render_to_response("sportsadmin/PlayerList.html",c)
    
@login_required(login_url='/loginAdmin/')	
def CoachList(request):
    print "start of CoachList"
    qs=request.user.groups.values_list("name",flat=True)
   
    querySet=None
    querySet1=None
    coach=None
    
    #Query to get coaches for particular Academy login
    if not qs:
	 # admin login
     coach = CoachTable(CoachOnboarding.objects.all())
    elif qs[0]=='common' and qs[1]:
     #province login
     print qs[0]
     print "province login"
     querySet=Province.objects.filter(province_name=qs[1])
     querySet1=Address.objects.filter(province=querySet[0].province_id)
     coach = CoachTable(CoachOnboarding.objects.filter(address__in =querySet1)) 
	 
    elif qs[1] and qs[0]!="common":
      print "academy login"
      queryset=AcademyOnboarding.objects.filter(name=qs[0])
      coach = CoachTable(CoachOnboarding.objects.filter(acd_reg=queryset[0].acd_reg_id))
        
    coachform=CoachOnBoardingForm()
    addressform=AddressForm()
    print coach
    c = {'CoachList':coach,'coachform':coachform,'addressform':addressform}
    c.update(csrf(request))
    return render_to_response("sportsadmin/CoachList.html",c)
   
@login_required(login_url='/loginAdmin/')
def AcademyList(request):
    print "start of AcademyList"
    qs=request.user.groups.values_list("name",flat=True)
   
    querySet=None
    querySet1=None
    academy=None
    
    #Query to get coaches for particular Academy login
    if not qs:
	 # admin login
     academy = AcademyTable(AcademyOnboarding.objects.all())
    elif qs[0]=='common' and qs[1]:
     print "province login"
     querySet=Province.objects.filter(province_name=qs[1])
     querySet1=Address.objects.filter(province=querySet[0].province_id)
     academy = AcademyTable(AcademyOnboarding.objects.filter(address__in =querySet1))
    elif qs[1] and qs[0]!="common":
     #academy login
      academy=AcademyOnboarding.objects.filter(name=qs[1])
      
      print qs[1]
      Academyform=AcademyOnboardingForm(initial={'acd_reg':academy[0].acd_reg_id,'address':academy[0].address.address_id,'name':academy[0].name,'estd':academy[0].estd,'email_id':academy[0].email_id,'contact_no':academy[0].contact_no,'website':academy[0].website})
      addressform=AddressForm(initial={'city':academy[0].address.city,'province':academy[0].address.province,'country':academy[0].address.country,'street1':academy[0].address.street1,'street2':academy[0].address.street2,'zipcode':academy[0].address.zipcode})
      Academyform.fields['name'].widget.attrs['readonly']=True
      addressform.fields['province'].widget.attrs['disabled']=True
      return render(request,"sportsadmin/viewAcademy.html", {'Academyform':Academyform,'addressform':addressform})
    
    	 
    
    Academyform=AcademyOnboardingForm()
    addressform=AddressForm()
    
    
    return render(request,"sportsadmin/AcademyList.html", {'AcademyList':academy,'Academyform':Academyform,'addressform':addressform})
   
@login_required(login_url='/loginAdmin/')	
def viewPlayer(request,playerId):
    playerId =request.GET.get('playerId')
    
    player = PlayerOnboarding.objects.get(player_id=playerId)
    modelDict={'player':model_to_dict(player),
               'address':model_to_dict(player.address),
               'country':model_to_dict(player.address.country),
               'city':model_to_dict(player.address.city),
               'province':model_to_dict(player.address.province),
               'genderVal':model_to_dict(player.gender),
               'sports':model_to_dict(player.sports),
               'sec_ques1':model_to_dict(player.sec_ques),
               'academy':model_to_dict(player.acd_reg),
               }
    return  JsonResponse(modelDict)
@login_required(login_url='/loginAdmin/')
def viewCoach(request,coachId):
    coachId =request.GET.get('coachId')
    coach = CoachOnboarding.objects.get(coach_id=coachId)
    
    modelDict={'coach':model_to_dict(coach),
               'address':model_to_dict(coach.address),
               'country':model_to_dict(coach.address.country),
               'city':model_to_dict(coach.address.city),
               'province':model_to_dict(coach.address.province),
               'genderVal':model_to_dict(coach.gender),
               'sports':model_to_dict(coach.sports),
               'sec_ques1':model_to_dict(coach.sec_ques),
               'academy':model_to_dict(coach.acd_reg),
               }
    return  JsonResponse(modelDict)
	
@login_required(login_url='/loginAdmin/')
def viewAcademy(request,academyId):
    academyId =request.GET.get('academyId')
    academy = AcademyOnboarding.objects.get(acd_reg_id=academyId)
    modelDict={'academy':model_to_dict(academy),
               'address':model_to_dict(academy.address),
               'country':model_to_dict(academy.address.country),
               'city':model_to_dict(academy.address.city),
               'province':model_to_dict(academy.address.province),
               }
    return  JsonResponse(modelDict)

@login_required(login_url='/loginAdmin/')
def viewVideo(request,videoId):
    
    videoId =request.GET.get('videoId')
    video = Carousel_video_video.objects.get(video_id=videoId)
    
    modelDict={'video':model_to_dict(video),
               'sports':model_to_dict(video.sports),
               'sports_subtype':model_to_dict(video.subtype),
               }
    return  JsonResponse(modelDict)
	
	
@transaction.atomic
@login_required(login_url='/loginAdmin/')
def addPlayer(request):
    
    context = RequestContext(request)  
    if request.method == 'POST':
        form = PlayerOnBoardingForm(request.POST)  
        print form.errors	
        action_type= request.POST['action_type']		
        AddrForm=AddressForm(request.POST)
        print form['acd_reg'].value()
        print AddrForm.errors 
        if action_type == "edit":
           player_id = request.POST['player_id']
           address_id = request.POST['address_id']
           
           player = PlayerOnboarding.objects.get(player_id=player_id)
           address = Address.objects.get(address_id=address_id)
        
           form=PlayerOnBoardingForm(request.POST, instance=player)
           AddrForm=AddressForm(request.POST, instance=address)
		 
        if AddrForm.is_valid() and form.is_valid() :		
            address = AddrForm.save() 
            player=form.save(commit=False)
            player.address = address           
            player.save()
            
        else :
           AddrForm.errors
           form.errors
    else :
          print request.method
    return HttpResponse("success")
	
@transaction.atomic
@login_required(login_url='/loginAdmin/')
def addVideo(request):
    
    context = RequestContext(request)  
    if request.method == 'POST':
        form = CarouselVideoForm(request.POST)  
        print form.errors	
        action_type= request.POST['action_type']		
       
       
        if action_type == "edit":
           
           video_id = request.POST['video_id']          
           
           video = Carousel_video_video.objects.get(video_id=video_id)

           form=CarouselVideoForm(request.POST, instance=video)
        if form.is_valid() :		          
            form.save()
            
        else :          
           form.errors
    else :
          print request.method
    return HttpResponse("success")


@login_required(login_url='/loginAdmin/')
def viewPhoto(request,pictureId):
    print "within view photo"
    pictureId =request.GET.get('pictureId')
    photo = Temp_Carousel_Picture.objects.get(picture_id=pictureId)
    print photo
    
    modelDict={'photo':model_to_dict(photo)}
    return JsonResponse(modelDict)
    #return render(request, 'sportsadmin/PictureList.html', {'photo': photo})
   
	
@transaction.atomic
@login_required(login_url='/loginAdmin/')
def addPhoto(request):
    print "start of addPhotoDetails method :"
    	
    if request.method == 'POST':
       
       
        form = CarouselPictureForm(request.POST,request.FILES) 
        print request.POST		
        print form.errors	      
        action_type= request.POST['action_type']		      
        if action_type == "edit":
           
           picture_id = request.POST['picture_id']          
           
           picture = Carousel_Picture.objects.get(picture_id=picture_id)
           form=CarouselPictureForm(request.POST, instance=picture)
		   
        
        photo=form.save(commit=False)
        photo.image = request.FILES['image']
       
        print photo.image		   
        photo.save()			 
       
            
           
    else :
          print request.method
          form.errors
    Photo="Photo"
    return render(request,"sportsadmin/sportsadminpage.html/",{'default_load_tab':Photo})

@transaction.atomic
@login_required(login_url='/loginAdmin/')
def addCoach(request):
    
    context = RequestContext(request)  
    if request.method == 'POST': 
        	
        form = CoachOnBoardingForm(request.POST)  
        print form.errors		
        action_type= request.POST['action_type']
        AddrForm=AddressForm(request.POST)
        print AddrForm.errors
        if action_type == "edit":
           
           coach_id = request.POST['coach_id']
           address_id = request.POST['address_id']
           
           coach = CoachOnboarding.objects.get(coach_id=coach_id)
           address = Address.objects.get(address_id=address_id)
        
           form=CoachOnBoardingForm(request.POST, instance=coach)
           AddrForm=AddressForm(request.POST, instance=address)
        if AddrForm.is_valid() and form.is_valid():
            		
            address = AddrForm.save()
            print address.address_id			
            coach=form.save(commit=False)
            coach.address = address
            coach.save()
            
        else :
           AddrForm.errors
           form.errors
    else :
          print request.method
    
    return HttpResponse("success")
@login_required(login_url='/loginAdmin/')
def editAcademy(request):
  context = RequestContext(request)  
  if request.method == 'POST': 
        print "within academy edit request"	
        form = AcademyOnboardingForm(request.POST)  
        print form.errors		
        action_type= request.POST['action_type']
        AddrForm=AddressForm(request.POST)
        print AddrForm.errors
        if action_type == "edit":
           print "within action"
           academy_id = request.POST['acd_reg']
           address_id = request.POST['address']
           print academy_id+" & "+address_id
           academy = AcademyOnboarding.objects.get(acd_reg_id=academy_id)
           address = Address.objects.get(address_id=address_id)
        
           form=AcademyOnboardingForm(request.POST, instance=academy)
           AddrForm=AddressForm(request.POST, instance=address)
           if AddrForm.is_valid() and form.is_valid():
            	
            address = AddrForm.save()
            print address.address_id			
            academy=form.save(commit=False)
            academy.address = address
            academy.save()
            print "save done"
  return HttpResponse("success")
@login_required(login_url='/loginAdmin/')
@transaction.atomic
def addAcademy(request):
    
    context = RequestContext(request)  
    if request.method == 'POST': 
        	
        form = AcademyOnboardingForm(request.POST)  
        print form.errors		
        action_type= request.POST['action_type']
        AddrForm=AddressForm(request.POST)
        print AddrForm.errors
        if action_type == "edit":
           
           academy_id = request.POST['academy_id']
           address_id = request.POST['address_id']
           
           academy = AcademyOnboarding.objects.get(acd_reg_id=academy_id)
           address = Address.objects.get(address_id=address_id)
        
           form=AcademyOnboardingForm(request.POST, instance=academy)
           AddrForm=AddressForm(request.POST, instance=address)
        if AddrForm.is_valid() and form.is_valid():
            	
            address = AddrForm.save()
            print address.address_id			
            academy=form.save(commit=False)
            academy.address = address
            academy.save()
            
        else :
           AddrForm.errors
           form.errors
    else :
          print request.method
   
    return HttpResponse("success")

@login_required(login_url='/loginAdmin/')	 
@transaction.atomic
def deletePhoto(request,pictureId):
    
    pictureId = request.GET.get('pictureId',None)
    if pictureId is None:
        
        return render_to_response("sportsadmin/exception.html", RequestContext(request,{}))
    else:
        
        Carousel_Picture.objects.filter(picture_id=pictureId).delete()
        
        
    return HttpResponse("success")
@login_required(login_url='/loginAdmin/')
@transaction.atomic
def deletePlayer(request,playerId):
    
    playerId = request.GET.get('playerId',None)
    if playerId is None:
        
        return render_to_response("sportsadmin/exception.html", RequestContext(request,{}))
    else:
        
        Address.objects.filter(address_id=(PlayerOnboarding.objects.filter(player_id=playerId))[0].address_id).delete()
        PlayerOnboarding.objects.filter(player_id=playerId).delete()
        
        
    return HttpResponse("success")
@login_required(login_url='/loginAdmin/')
@transaction.atomic
def deleteVideo(request,videoId):
    
    videoId = request.GET.get('videoId',None)
    if videoId is None:
        
        return render_to_response("sportsadmin/exception.html", RequestContext(request,{}))
    else:
        
        Carousel_video_video.objects.filter(video_id=videoId).delete()
        
        
    return HttpResponse("success")
@login_required(login_url='/loginAdmin/')	
@transaction.atomic
def deleteCoach(request,coachId):
    
    coachId = request.GET.get('coachId',None)
    if coachId is None:
        
        return render_to_response("sportsadmin/exception.html", RequestContext(request,{}))
    else:
        
        Address.objects.filter(address_id=(CoachOnboarding.objects.filter(coach_id=coachId))[0].address_id).delete()
        CoachOnboarding.objects.filter(coach_id=coachId).delete()
        
        
    return HttpResponse("success")
@login_required(login_url='/loginAdmin/')	
@transaction.atomic
def deleteAcademy(request,academyId):
    
    academyId = request.GET.get('academyId',None)
    if academyId is None:
        
        return render_to_response("sportsadmin/exception.html", RequestContext(request,{}))
    else:
        
        Address.objects.filter(address_id=(AcademyOnboarding.objects.filter(acd_reg_id=academyId))[0].address_id).delete()
        AcademyOnboarding.objects.filter(acd_reg_id=academyId).delete()
        
        
    return HttpResponse("success")
