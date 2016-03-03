from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

class CMSSearchMatchPlugin(CMSPluginBase):
    module = _("searchMatch")
    name = _("searchMatch")  #name of the plugin in the interface
    render_template = "searchMatch/searchMatch.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSSearchMatchPlugin)  #register the plugin