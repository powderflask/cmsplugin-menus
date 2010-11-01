from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase

__all__ = ("CMSPLUGIN_MENUS_TEMPLATE_PATH", "_get_template_path", "_MenuPluginBase")
CMSPLUGIN_MENUS_TEMPLATE_PATH = "cmsplugin_menus/"
CMSPLUGIN_MENUS_ICON_PATH = "%s%s"%(settings.MEDIA_URL, u"cmsplugin_menus/images/")


def _get_template_path(template_file):
    return "%s%s"%(CMSPLUGIN_MENUS_TEMPLATE_PATH, template_file)

class _MenuPluginBase(CMSPluginBase):
    """
        Abstract base class for Menu plugins.
    """
    model = CMSPlugin
    module="Menus"
    text_enabled = getattr(settings, "CMSPLUGIN_MENU_TEXT_ENABLED", False);    icon_file = "hierarchy.png"
    icon_file = None

    def render(self, context, instance, placeholder):
        """ default render for template logic-only plugins """
        return context

    def icon_src(self, instance):
        if self.icon_file:
            return "%s%s"%(CMSPLUGIN_MENUS_ICON_PATH, self.icon_file)
        else:
            return None
