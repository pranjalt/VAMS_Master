from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class rotatingAdsAppPlugin(CMSPluginBase):
    module = _("rotatingAds")
    name = _("rotatingAds")  # name of the plugin in the interface
    render_template = "rotatingAds/rotatingAds.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(rotatingAdsAppPlugin)  # register the plugin