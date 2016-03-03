from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class lowerFooterAppPlugin(CMSPluginBase):
    module = _("lowerFooterApp")
    name = _("lowerFooterApp")  # name of the plugin in the interface
    render_template = "lowerFooterApp/lowerFooterApp.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(lowerFooterAppPlugin)  # register the plugin