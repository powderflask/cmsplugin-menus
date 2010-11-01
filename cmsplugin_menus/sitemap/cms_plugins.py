from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cmsplugin_menus.cms_plugins import *

class SitemapPlugin(_MenuPluginBase):
    """
        Plugin to display a basic site map.
    """
    name = _("Sitemap")
    render_template = _get_template_path("sitemap.html")

plugin_pool.register_plugin(SitemapPlugin)
