from django.db import models
from django.contrib.auth.models import User
#from cms.models.pluginmodel import CMSPlugin
from cms.models import CMSPlugin
from sportsList.models import Onboarding,Sports
		

class CwgOnboardingPlugin(CMSPlugin):
		onboarding = models.ForeignKey(Onboarding)
    #sports = models.ForeignKey(Sports)