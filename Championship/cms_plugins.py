from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class CMSChampionshipPlugin(CMSPluginBase):
    module = _("Championship")
    name = _("Championship Plugin")  # name of the plugin in the interface
    render_template = "championship_plugin/championship_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSChampionshipPlugin)  # register the plugin