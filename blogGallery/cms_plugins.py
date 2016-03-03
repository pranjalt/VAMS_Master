from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class BlogGalleryPlugin(CMSPluginBase):
    module = _("blogGallery")
    name = _("blogGallery")  # name of the plugin in the interface
    render_template = "blogGallery/blogGallery.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(BlogGalleryPlugin)  # register the plugin