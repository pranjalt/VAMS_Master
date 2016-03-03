from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSLowerFooterPlugin(CMSPluginBase):
    module = _("Lower Footer")
    name = _("Lower Footer Plugin")  # name of the plugin in the interface
    render_template = "lowerFooter_plugin/lowerFooter_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSLowerFooterPlugin)  # register the plugin