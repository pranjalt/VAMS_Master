from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class socaPlugin(CMSPluginBase):
    module = _("socaPlugin")
    name = _("socaPlugin")  # name of the plugin in the interface
    render_template = "socaPlugin/socaPlugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(socaPlugin)  # register the plugin