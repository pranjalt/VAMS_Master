from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
#from models import CwgOnboardingPlugin
#from models import Hello
from .models import *
from sportsList.models import *
from assetManagement.forms import *

from django.db.models import Count

class assetManagementForm(CMSPluginBase):
    name=_('assetManagementForm')
    render_template = "assetManagement/AssetMgmtForm.html"
    cache = False
	
    def render(self, context, instance, placeholder):
         context.update({'instance': instance,'Assetform':AssetManagementForm()})
	   
         return context
plugin_pool.register_plugin(assetManagementForm) 
