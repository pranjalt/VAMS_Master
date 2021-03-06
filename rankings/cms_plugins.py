from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class rankings(CMSPluginBase):
    module = _("rankings")
    name = _("rankings")  # name of the plugin in the interface
    render_template = "rankings/rankings.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(rankings)  # register the plugin