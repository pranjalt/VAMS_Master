from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSNewsBlogPlugin(CMSPluginBase):
    module = _("News & Blog")
    name = _("News_Blog Plugin")  # name of the plugin in the interface
    render_template = "news_Blog_plugin/news_Blog_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSNewsBlogPlugin)  # register the plugin