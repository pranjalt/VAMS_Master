from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class videoappPlugin(CMSPluginBase):
    module = _("videoapp")
    name = _("videoapp")  # name of the plugin in the interface
    render_template = "videoapp/videoapp.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(videoappPlugin)  # register the plugin