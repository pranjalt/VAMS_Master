from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from registerApp.forms import RegisterForm
from models import AppPLugin


class CMSRegPlugin(CMSPluginBase):
    module = _("RegisterApp")
    name = _("RegisterAppPlugin")  # name of the plugin in the interface
    render_template = "registerAppPlugin/registerAppPlugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance,'form':RegisterForm()})
        return context

plugin_pool.register_plugin(CMSRegPlugin)  # register the plugin