from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSCommonPlugin(CMSPluginBase):
    module = _("Common")
    name = _("Common")  # name of the plugin in the interface
    render_template = "common/common.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSCommonPlugin)  # register the plugin