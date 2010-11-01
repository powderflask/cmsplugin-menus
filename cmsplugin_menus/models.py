from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.utils.helpers import reversion_register
from cms.models.fields import PlaceholderField
from cmsplugin_menus import constants

class LinkBlock(models.Model):
    """
     A placeholder to be used for building a re-usable block of links. 
    """
    title = models.CharField(_("menu title"), max_length=255, unique=True, db_index=True)
    links = PlaceholderField(constants.CMSPLUGIN_MENUS_LINK_BLOCK_PLACEHOLDER, help_text=_("Add links, e-mails, snippets to the menu."))

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _("Custom Menu")
        verbose_name_plural = _("Custom Menus")
reversion_register(LinkBlock)

