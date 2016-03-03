from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSFooterPlugin(CMSPluginBase):
    module = _("Footer")
    name = _("Footer Plugin")  # name of the plugin in the interface
    render_template = "footer_plugin/footer_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSFooterPlugin)  # register the plugin