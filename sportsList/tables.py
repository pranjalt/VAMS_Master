import django_tables2 as tables
from .models import PlayerOnboarding,Sports
from django.db.models import Count

#from django_tables2_simplefilter import F
class PlayerOnboardingTable(tables.Table):
    class Meta:
        model = PlayerOnboarding
        attrs = {'class': 'table table-condensed table-vertical-center paleblue', 'id': 'dashboard_table'}
        exclude = ("player_id","middle_name", "sec_ques","sec_ans1","sec_ans2")
        #filters = (F('field','Filter name',values_list=[ (str(x), x.first_name) for x in Onboarding.objects.all()]))

class SportsTable(tables.Table):
    
    Count = tables.Column()
    class Meta:
        model = Sports
        attrs = {'class': 'table table-condensed table-vertical-center paleblue', 'id': 'dashboard_table'}
        exclude = ("sports_id",)