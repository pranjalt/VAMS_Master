from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSSportPlugin(CMSPluginBase):
    module = _("SportListPlugin")
    name = _("sportList Plugin")  # name of the plugin in the interface
    render_template = "sportListPlugin/sportListPlugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSSportPlugin)  # register the plugin