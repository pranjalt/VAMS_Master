from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

class CMSCurrentMatchStatsPlugin(CMSPluginBase):
    module = _("currentMatchStats")
    name = _("currentMatchStats")  #name of the plugin in the interface
    render_template = "currentMatchStats/currentMatch.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSCurrentMatchStatsPlugin)  #register the plugin