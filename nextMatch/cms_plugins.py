from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSNextMatchPlugin(CMSPluginBase):
    module = _("nextMatch")
    name = _("nextMatch")  # name of the plugin in the interface
    render_template = "nextMatch/nextMatch.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSNextMatchPlugin)  # register the plugin