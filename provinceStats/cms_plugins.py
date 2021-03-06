from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class provinceStatsPlugin(CMSPluginBase):
    module = _("provinceStats")
    name = _("provinceStats")  # name of the plugin in the interface
    render_template = "provinceStats/provinceStats.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(provinceStatsPlugin)  # register the plugin