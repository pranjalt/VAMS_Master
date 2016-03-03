from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class homeBlogsPlugin(CMSPluginBase):
    module = _("homeBlogs")
    name = _("homeBlogs")  # name of the plugin in the interface
    render_template = "homeBlogs/homeBlogs.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(homeBlogsPlugin)  # register the plugin