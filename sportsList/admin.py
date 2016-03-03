from django.contrib import admin

# Register your models here.
from .models import AcademyOnboarding,PlayerOnboarding,CoachOnboarding

class AcademyOnboardingAdmin(admin.ModelAdmin):
  model=AcademyOnboarding
  exclude =('acd_reg_id',)
    

admin.site.register(AcademyOnboarding, AcademyOnboardingAdmin)

class PlayerOnboardingAdmin(admin.ModelAdmin):
  model=PlayerOnboarding
  exclude =('player_id','address')
    

admin.site.register(PlayerOnboarding, PlayerOnboardingAdmin)

class CoachOnboardingAdmin(admin.ModelAdmin):
  model=CoachOnboarding
  exclude =('coach_id','address')
    

admin.site.register(CoachOnboarding,CoachOnboardingAdmin)