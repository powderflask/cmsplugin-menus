from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cmsplugin_menus.cms_plugins import *
from models import LinkBlockPtr
    
class LinkBlockPlugin(_MenuPluginBase):
    model = LinkBlockPtr
    name = _("Custom Menu")
    render_template = _get_template_path("link_block.html")
    icon_file = "linkblock.png"
    
    def render(self, context, instance, placeholder):
        context.update({
            'collapse' : instance.collapse,
            'link_block': instance.link_block,
        })
        return context
plugin_pool.register_plugin(LinkBlockPlugin)
