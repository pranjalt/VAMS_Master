import django_filters
from .models import PlayerOnboarding,Sports

class PlayerOnboardingFilter(django_filters.FilterSet):
    class Meta:
        model = PlayerOnboarding
        fields = ['first_name', 'total_yrs_exp',]
    
class SportsFilter(django_filters.FilterSet):
    class Meta:
        model = Sports
        fields = ['sports_name']