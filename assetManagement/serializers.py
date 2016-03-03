from rest_framework import serializers
from sportsList.models import Sports
from .models import *


class VendorsSerializer(serializers.ModelSerializer):
    #vendor = serializers.CharField(read_only=True)
    class Meta:
        model = Vendor
        fields=('name','vendor_id')
    
class SportsSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(read_only=True)
    class Meta:
         model = Sports
         fields=('sports_name',)
		
class VendorSportsSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(source='sports.sports_name',read_only=True)
    class Meta:
        model = VendorSports
        fields = ('sports','sports_name')

class AssetSerializer(serializers.ModelSerializer):
    asset = serializers.CharField(read_only=True)
    class Meta:
         model = Asset
         fields=('asset',)
		
class VendorsportsAssetSerializer(serializers.ModelSerializer):
    asset = serializers.CharField(source='asset.asset',read_only=True)
    class Meta:
        model = VendorsportsAsset
        fields = ('vendor_sport','asset')
		
class SchoolSerializer(serializers.ModelSerializer):
    school = serializers.CharField(read_only=True)
    class Meta:
        model = School
        fields = ('school_name','school')


class AssetmanagementSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source='vendor.name',read_only=True)
    sports = serializers.CharField(source='sports.sports_name',read_only=True)
    asset = serializers.CharField(source='asset.asset',read_only=True)
    school = serializers.CharField(source='school.school_name',read_only=True)
    class Meta:
        model = Assetmanagement
        fields = ('sports','asset','asset_quantity','vendor','school','issue_date','return_date')
