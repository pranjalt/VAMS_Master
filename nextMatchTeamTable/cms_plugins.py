from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class NextMatchTeamTablePlugin(CMSPluginBase):
    module = _("nextMatchTeamTable")
    name = _("nextMatchTeamTable")  # name of the plugin in the interface
    render_template = "nextMatchTeamTable/nextMatchTeamTable.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(NextMatchTeamTablePlugin)  # register the plugin