from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSCarouselPlugin(CMSPluginBase):
    module = _("Carousel")
    name = _("Carousel Plugin")  # name of the plugin in the interface
    render_template = "carousel_plugin/carousel_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSCarouselPlugin)  # register the plugin