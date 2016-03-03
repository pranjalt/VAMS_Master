from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

class ShopPlugin(CMSPluginBase):
    module = _("shop")
    name = _("shop")  #name of the plugin in the interface
    render_template = "shop/shop.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ShopPlugin)  #register the plugin