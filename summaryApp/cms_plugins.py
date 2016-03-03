from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class summaryAppPlugin(CMSPluginBase):
    module = _("summaryApp")
    name = _("summaryApp")  # name of the plugin in the interface
    render_template = "summaryApp/summaryApp.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(summaryAppPlugin)  # register the plugin