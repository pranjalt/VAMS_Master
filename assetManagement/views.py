from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from rest_framework import viewsets
from .serializers import VendorsSerializer, VendorSportsSerializer, VendorsportsAssetSerializer, AssetmanagementSerializer
from rest_framework.decorators import *
from rest_framework import generics
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets
from assetManagement.models import *
from sportsList.models import *
from assetManagement.serializers import *
from dateutil import parser

# Create your views here.
class get_vendor_list_ws(generics.ListCreateAPIView):
	print"in vendor method WS"
	#vendor_id = request.GET['vendor_id']
	queryset = Vendor.objects.all()	
	serializer_class = VendorsSerializer
	print 'vendor done'
	
class get_sports_by_vendor_ws(viewsets.ModelViewSet):
    def get_queryset(self):
        vendor_id = self.request.query_params.get('vendor_id')

        queryset = VendorSports.objects.filter(vendor=vendor_id).prefetch_related('sports') 
        return queryset
    serializer_class = VendorSportsSerializer
	

class get_assets_by_vendorSports_ws(viewsets.ModelViewSet):
  
    def get_queryset(self):
        vendor_id = self.request.query_params.get('vendor_id')
        sports_id = self.request.query_params.get('sports_id')
        queryset = VendorSports.objects.get(vendor=vendor_id,sports=sports_id)
        vendorSportsId= queryset.vendorsport_id
        print "vendor sports Id jdadjaadasdaass"
        print vendorSportsId
        queryset = VendorsportsAsset.objects.filter(vendor_sport = vendorSportsId).prefetch_related('asset') 
        return queryset
		
    serializer_class = VendorsportsAssetSerializer
	

class assets_distribution_list_ws(generics.ListCreateAPIView):
    queryset = Assetmanagement.objects.all().prefetch_related('sports','asset','school','vendor') 
    print "in asset Mgmt Service"
    serializer_class = AssetmanagementSerializer
    
class school_list_ws(generics.ListCreateAPIView):
    queryset = School.objects.all()
    print "school_list_ws"
    serializer_class = SchoolSerializer
 
 
class create_asset_management_ws(viewsets.ModelViewSet):
   queryset = Assetmanagement.objects.all()
   serializer_class = AssetmanagementSerializer
   def create(self, request):
         vendor_id = request.data.get('vendor_id', None)
         sports_id = request.data.get('sports_id', None)
         asset_id = request.data.get('asset_id', None)
         school_id = request.data.get('school_id', None)
   
         if vendor_id and sports_id and asset_id and school_id :
              #obj = ClassTeacherSubjectMap.objects.get(class_class=class_id,teacher_information_teacher=teacher_id,subject_subject=subject_id)
              quentity = request.data.get('quentity', '')
              issue_date = request.data.get('issue_date', '')
              return_date = request.data.get('return_date', '')
              iss_date = parser.parse(issue_date)
              rtn_date = parser.parse(return_date)
              new_obj = Assetmanagement(vendor=vendor_id,sports=sports_id,asset=asset_id,school=school_id,asset_quantity=quentity,issue_date=issue_date,return_date=return_date)
              new_obj.save()
              serializer = self.get_serializer(new_obj)
              return Response(serializer.data)
         return HttpResponse("Please provide teacher/class/subject ID. properly")
