from rest_framework import serializers
from sportsList.models import Sports
from .models import *
class SportSubtypeSerializer(serializers.ModelSerializer):
    sports_subtype = serializers.CharField(read_only=True)
    class Meta:
        model = SportsSubtype
        fields = ('subtype_id','sports','sports_subtype',)
class SportSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(read_only=True)
    class Meta:
        model = Sports
        fields = ('sports_name',)
      
class VideoListSerializer(serializers.ModelSerializer):
    sports_name = serializers.CharField(source='sports.sports_name', read_only=True)
    sports_subtype = serializers.CharField(source='subtype.sports_subtype', read_only=True)
    
    class Meta:
        model = Carousel_video_video
        fields = ('movie', 'movie_url', 'image','width','height','auto_play','auto_hide','fullscreen','loop','bgcolor','textcolor','seekbarcolor','seekbarbgcolor','loadingbarcolor','buttonoutcolor','buttonovercolor','buttonhighlightcolor','sports_name','sports_subtype')
        

        
