from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class InformationPlugin(CMSPluginBase):
    name = _("Information Plugin")  # name of the plugin in the interface
    render_template = "information/information.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(InformationPlugin)  # register the plugin