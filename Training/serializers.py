from rest_framework import serializers
from .models import *
from sportsList.serializers import *
class BatchSerializer(serializers.ModelSerializer):
    batch_name = serializers.CharField(read_only=True)
    class Meta:
        model = Batch
        fields = ('batch_id','batch_name')
        
        
class StageSerializer(serializers.ModelSerializer):
    stage_name = serializers.CharField(read_only=True)
    class Meta:
        model = Stage
        fields = ('stage_id','stage_name')
        
class TrainingSerializer(serializers.ModelSerializer):
    address=AddSerializer()  
    player=PlayerListSerializer()
    stage_name = serializers.CharField(source='stage.stage_name', read_only=True)
    sports_name = serializers.CharField(source='sports.sports_name', read_only=True)
    batch_name = serializers.CharField(source='batch.batch_name', read_only=True)
    class Meta:
        model = Training
        fields = ('coach','sports_name','player','batch_name','stage_name','address','training_date','training_time')
      
   