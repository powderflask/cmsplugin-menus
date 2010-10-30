from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_menus.models import LinkBlockPtr, NavMenu

CMSPLUGIN_MENS_TEMPLATE_PATH = "cmsplugin_menus/"

def _get_template_path(template_file):
    return "%s%s"%(CMSPLUGIN_MENS_TEMPLATE_PATH, template_file)

class MenuPluginBase(CMSPluginBase):
    """
        Abstract basc class for Menu plugins.
    """
    model = CMSPlugin
    module="Menus"
    text_enabled = getattr(settings, "CMSPLUGIN_MENU_TEXT_ENABLED", False);

    def render(self, context, instance, placeholder):
        """ default render for template logic-only plugins """
        return context
    
class LinkBlockPlugin(MenuPluginBase):
    model = LinkBlockPtr
    name = _("Custom Menu")
    render_template = _get_template_path("link_block.html")
    
    def render(self, context, instance, placeholder):
        context.update({
            'collapse' : instance.collapse,
            'link_block': instance.link_block,
        })
        return context
plugin_pool.register_plugin(LinkBlockPlugin)


class NavMenuPlugin(MenuPluginBase):
    model = NavMenu
    name = _("Section Nav. Menu")
    render_template = _get_template_path("nav_menu.html")
    
    def render(self, context, instance, placeholder):
        context.update({
            'title': instance.title,
            'collapse' : instance.collapse,
            'subsection' : instance.section,
        })
        return context
plugin_pool.register_plugin(NavMenuPlugin)


class SitemapPlugin(MenuPluginBase):
    """
        Plugin to display a basic site map.
    """
    name = _("Sitemap")
    render_template = _get_template_path("sitemap.html")

plugin_pool.register_plugin(SitemapPlugin)
