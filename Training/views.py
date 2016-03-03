from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from serializers import *
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
	
class BatchList(viewsets.ModelViewSet):   
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    
class StageList(viewsets.ModelViewSet):   
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    
class TrainingRegister(viewsets.ModelViewSet):   
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class TrainingBatch(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Training.objects.all()
        batch_name= self.request.query_params.get('batch_name', None) 
        batch_id=Batch.objects.filter(batch_name=batch_name)
        print batch_id[0].batch_id
        if batch_name is not None:      
          queryset = queryset.filter(batch_id=batch_id[0].batch_id)  		  
        return queryset
    serializer_class = TrainingSerializer
    pagination_class = StandardResultsSetPagination
# Create your views here.


class TrainingPlayer(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = Training.objects.all()
        player_id= self.request.query_params.get('player_id', None)         
        if player_id is not None:      
          queryset = queryset.filter(player_id=player_id)            
        return queryset
    serializer_class = TrainingSerializer
    pagination_class = StandardResultsSetPagination
    
class TrainingCoach(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        queryset = Training.objects.all()
        coach_id= self.request.query_params.get('coach_id', None)         
        if coach_id is not None:      
          queryset = queryset.filter(coach_id=coach_id)            
        return queryset
		