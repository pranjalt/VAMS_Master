from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class topProvincePlugin(CMSPluginBase):
    module = _("topProvince")
    name = _("topProvince")  # name of the plugin in the interface
    render_template = "topProvince/topProvince.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(topProvincePlugin)  # register the plugin