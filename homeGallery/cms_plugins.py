from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class homeGalleryPlugin(CMSPluginBase):
    module = _("homeGallery")
    name = _("homeGallery")  # name of the plugin in the interface
    render_template = "homeGallery/homeGallery.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(homeGalleryPlugin)  # register the plugin