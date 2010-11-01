from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.utils.helpers import reversion_register
from cms.models.fields import PlaceholderField
from cmsplugin_menus.constants import CMSPLUGIN_MENUS_LINK_BLOCK_PLACEHOLDER

class LinkBlock(models.Model):
    """
     A placeholder to be used for building a re-usable block of links. 
    """
    title = models.CharField(_("menu title"), max_length=255, unique=True, db_index=True)
    links = PlaceholderField(CMSPLUGIN_MENUS_LINK_BLOCK_PLACEHOLDER, help_text=_("Add links, e-mails, snippets to the menu."))

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _("Custom Menu")
        verbose_name_plural = _("Custom Menus")
reversion_register(LinkBlock)

class LinkBlockPtr(CMSPlugin):
    """
      Plugin model for a Custom Menu (Link Block)
      To limit plugins to links, relies on setting:
      CMS_PLACEHOLDER_CONF = {
        ...
        'cmsplugin_menus link block': {
                'plugins': ('LinkPlugin', 'SnippetPlugin', ...),
                'name': gettext("links")
        }}
    """
    link_block = models.ForeignKey(LinkBlock)
    collapse = models.BooleanField(_("collapse menu"), default=False, help_text="Select this option if the menu should initially appear collapsed.")

    class Meta:
        verbose_name = _("Custom Menu Plugin Model")

    def __unicode__(self):
        return self.link_block.title
reversion_register(LinkBlockPtr)
