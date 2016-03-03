from django.db import models
from sportsList.models import Sports,CoachOnboarding,PlayerOnboarding,Address


class Batch(models.Model):
    batch_id = models.IntegerField(primary_key=True)
    batch_name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'batch'
        
    def __str__(self):
        return self.batch_name

class Stage(models.Model):
    stage_id = models.IntegerField(primary_key=True)
    stage_name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'stage'
    def __str__(self):
        return self.stage_name
        
class Training(models.Model):
    training_id = models.IntegerField(primary_key=True)
    coach = models.ForeignKey(CoachOnboarding, db_column='coach', blank=True, null=True)
    sports = models.ForeignKey(Sports, db_column='sports', blank=True, null=True)
    player = models.ForeignKey(PlayerOnboarding, db_column='player', blank=True, null=True)
    batch = models.ForeignKey(Batch, db_column='batch', blank=True, null=True)
    stage = models.ForeignKey(Stage, db_column='stage', blank=True, null=True)
    address = models.ForeignKey(Address, db_column='address', blank=True, null=True)
    training_date = models.DateField(blank=True, null=True)
    training_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training'