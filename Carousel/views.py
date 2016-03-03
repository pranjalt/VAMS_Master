from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from serializers import *
from rest_framework import viewsets
from rest_framework import generics

    
class VideoList(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Carousel_video_video.objects.all()
        sports_name= self.request.query_params.get('sports_name', None) 
        sports_id=Sports.objects.filter(sports_name=sports_name)
        print sports_id[0].sports_id
		
        sports_subtype = self.request.query_params.get('sports_subtype', None)
        subtype_id=SportsSubtype.objects.filter(sports_subtype=sports_subtype)	
        print subtype_id[0].subtype_id			
        if sports_name and sports_subtype is not None:      
          queryset = queryset.filter(sports_id=sports_id[0].sports_id,subtype_id=subtype_id[0].subtype_id)            
        return queryset
    serializer_class = VideoListSerializer 
    
    
    
		
class SportSubtype(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = SportsSubtype.objects.all()
        sports_name= self.request.query_params.get('sports_name', None) 
        sports_id=Sports.objects.filter(sports_name=sports_name)
        print sports_id[0].sports_id
        if sports_name is not None:      
          queryset = queryset.filter(sports_id=sports_id[0].sports_id)            
        return queryset
    serializer_class = SportSubtypeSerializer
    
        
class Sport(viewsets.ModelViewSet):
   queryset = Sports.objects.all()
   serializer_class = SportSerializer
   