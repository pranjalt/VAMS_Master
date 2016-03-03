from django.shortcuts import render_to_response,render
from django.http import HttpResponse
#from .models import Sports
from django.db.models import Count
from sportsList.models import *
# Create your views here.

"""def sports_list(request):
    sport_list = Sports.objects.all()
    html = ""
    #for sport in sport_list:
    #   html += "%s :: %s <br/>" % (sport.sports_name)
    print html
    #return HttpResponse("Test")
    #context_instance=RequestContext(request) 	
    return render(request,'cwgsportslist/sportsList.html',{'sport_list':sport_list}) """

	
def getPlayersListData(request):	
   print 'within getPlayersListData'
   sport = request.GET.get('sport', '')
   players = [] 
   if sport:
		players = Onboarding.objects.filter(sports__sports_name=sport)
   for player in players :
		print player.date_of_birth
   return render_to_response("players/test.html",{'players':players})