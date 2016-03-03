from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class sponsorsPlugin(CMSPluginBase):
    module = _("sponsorsPlugin")
    name = _("sponsorsPlugin")  # name of the plugin in the interface
    render_template = "sponsorsPlugin/sponsorsPlugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(sponsorsPlugin)  # register the plugin