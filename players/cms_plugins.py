from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from models import CwgOnboardingPlugin
#from models import Hello
from forms import OnBoardingForm
from sportsList.models import Sports
from django.db.models import Count

class UserCwgSportsPlugin(CMSPluginBase):
    name = _('UserCwgSports')
    model = CwgOnboardingPlugin	
    render_template = "players/playersRegistrationForm.html"
    cache = False
	
    def render(self, context, instance, placeholder):
         context.update({'instance': instance,'form':OnBoardingForm(),'model':CwgOnboardingPlugin})
         return context

plugin_pool.register_plugin(UserCwgSportsPlugin)


class sportsListPlugin(CMSPluginBase):
    name = _('getSportsList')
    render_template = "players/players.html"
    cache = False
			
    def render(self, context, instance, placeholder):
         sport_list = Sports.objects.annotate(reg_count=Count('onboarding'))
         context.update({'instance': instance,'sport_list':sport_list})
         return context

plugin_pool.register_plugin(sportsListPlugin)
