from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class footerAppPlugin(CMSPluginBase):
    module = _("footerApp")
    name = _("footerApp")  # name of the plugin in the interface
    render_template = "footerApp/footerApp.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(footerAppPlugin)  # register the plugin