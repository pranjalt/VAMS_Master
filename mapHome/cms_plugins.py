from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class MapHomePlugin(CMSPluginBase):
    module = _("mapHome")
    name = _("mapHome")  # name of the plugin in the interface
    render_template = "mapHome/mapHome.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(MapHomePlugin)  # register the plugin