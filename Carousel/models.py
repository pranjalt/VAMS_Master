import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sportsList.models import Sports
from cms.models import CMSPlugin
try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path on django CMS 3.0.4+ for information
        """
        return instance.get_media_path(filename)
from cms.utils.compat.dj import python_2_unicode_compatible
get_media=settings.MEDIA_ROOT

class SportsSubtype(models.Model):
   subtype_id=models.AutoField(primary_key=True)
   sports = models.ForeignKey(Sports,blank=True, null=True)
   sports_subtype = models.CharField(max_length=30, blank=True, null=True)

   def __str__(self):
        return self.sports_subtype
   class Meta:
        managed = True
        db_table = 'Carousel_subtype'
   
  


class Carousel_video_video(models.Model):   
    video_id = models.AutoField(primary_key=True)
    movie = models.CharField(max_length=100,blank=True,null=True)
    movie_url = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=100,blank=True,null=True)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    auto_play = models.BooleanField(default=False)
    auto_hide = models.BooleanField(default=False)
    fullscreen = models.BooleanField(default=True)
    loop = models.BooleanField(default=False)
    bgcolor = models.CharField(max_length=6,default="000000")
    textcolor = models.CharField(max_length=6,default="FFFFFF")
    seekbarcolor = models.CharField(max_length=6,default="13ABEC")
    seekbarbgcolor = models.CharField(max_length=6,default="333333")
    loadingbarcolor = models.CharField(max_length=6,default="828282")
    buttonoutcolor = models.CharField(max_length=6,default="333333")
    buttonovercolor = models.CharField(max_length=6,default="000000")
    buttonhighlightcolor = models.CharField(max_length=6,default="FFFFFF")
    sports=models.ForeignKey(Sports,blank=True, null=True)
    subtype=models.ForeignKey(SportsSubtype,blank=True, null=True)

        
    class Meta:
        managed = True
        db_table = 'Carousel_video_video'


	  
    def __str__(self):
        if self.movie:
            name = self.movie.path
        else:
            name =""
        return (name)
		
	def get_fullscreen(self):
		return "%s" % self.fullscreen
	
    def get_height(self):
        return "%s" % self.height
    
    def get_width(self):
        return "%s" % self.width
    
    def get_movie(self):
        if self.movie:
            return self.movie.url
        else:
            return ""
			
class Carousel_Picture(models.Model):
    LEFT = "left"
    RIGHT = "right"
    CENTER = "center"
    FLOAT_CHOICES = ((LEFT, _("left")),
                     (RIGHT, _("right")),
                     (CENTER, _("center")),
                     )
    picture_id = models.AutoField(primary_key=True)
    image = models.FileField(max_length=100,blank=True,upload_to=get_media)
    url = models.CharField(max_length=255, blank=True)
    alt = models.CharField(max_length=255, blank=True)
    longdesc = models.CharField(max_length=255, blank=True)
    float = models.CharField(max_length=10, blank=True,choices=FLOAT_CHOICES)
   
    class Meta:
        managed = False
        db_table = 'Carousel_picture_picture'
		
    def __str__(self):
        if self.image:
			name = self.image
        else:
            name =""
        return str(name)

class Temp_Carousel_Picture(models.Model): 
    picture_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=100,blank=True)
    url = models.CharField(max_length=255, blank=True)
    alt = models.CharField(max_length=255, blank=True)
    longdesc = models.CharField(max_length=255, blank=True)
    float = models.CharField(max_length=10, blank=True)
   
    class Meta:
        managed = False
        db_table = 'Carousel_picture_picture'
		
    def __str__(self):
        if self.image:
			name = self.image
        else:
            name =""
        return str(name)
