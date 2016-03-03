from django.db import models
from django.contrib.auth.models import User
from cms.models.pluginmodel import CMSPlugin
from cms.models import CMSPlugin
from sportsList.models import Sports

class Asset(models.Model):
    asset_id = models.AutoField(primary_key=True)
    asset = models.CharField(max_length=45)

    def __str__(self):
        return self.asset
    class Meta:
        managed = True
        db_table = 'asset'
    


class School(models.Model):
    school_id = models.AutoField(primary_key=True)  # AutoField?
    school_name = models.CharField(max_length=45)
    def __str__(self):
        return self.school_name
    class Meta:
        managed = True
        db_table = 'school'
    

class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'vendor'
    def __str__(self):
        return self.school_name
   

class VendorSports(models.Model):
    vendorsport_id = models.AutoField(primary_key=True)  # AutoField?
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    sports = models.ForeignKey('sportsList.Sports',on_delete=models.CASCADE,related_name='sport1')
    
    class Meta:
        managed = True
        db_table = 'vendor_sports'

class VendorsportsAsset(models.Model):
    vendorsport_asset_id = models.AutoField(primary_key=True)  # AutoField?
    max_quantity = models.IntegerField(blank=True, null=True)
    quantity_left = models.IntegerField(blank=True, null=True)
    asset = models.ForeignKey(Asset, blank=True, null=True)
    vendor_sport = models.ForeignKey(VendorSports,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vendorsports_asset'

class Assetmanagement(models.Model):
    asset_mgmt_id = models.AutoField(primary_key=True)  # AutoField?
    asset_quantity = models.IntegerField(blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE,blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,blank=True, null=True)
    sports = models.ForeignKey('sportsList.Sports', on_delete=models.CASCADE,blank=True, null=True,related_name='sport2')
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assetmanagement'

