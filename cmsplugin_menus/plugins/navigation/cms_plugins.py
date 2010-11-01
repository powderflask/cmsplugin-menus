from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cmsplugin_menus.cms_plugins import *
from models import NavMenu

class NavMenuPlugin(_MenuPluginBase):
    model = NavMenu
    name = _("Section Nav. Menu")
    render_template = _get_template_path("nav_menu.html")
    icon_file = "hierarchy.png"

    def render(self, context, instance, placeholder):
        context.update({
            'title': instance.title,
            'collapse' : instance.collapse,
            'subsection' : instance.section,
        })
        return context
plugin_pool.register_plugin(NavMenuPlugin)
