from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from cms.utils.helpers import reversion_register
from cms.models.fields import PlaceholderField

"""
    Custom menu plugins for Django CMS.
"""

class LinkBlock(models.Model):
    """
     A placeholder to be used for building a re-usable block of links. 
     To limit plugins to links, relies on setting:
     CMS_PLACEHOLDER_CONF = {
        'link-block': {
                'plugins': ('LinkPlugin', 'SnippetPlugin', ...),
                'name': gettext("links")
        }}
    """
    title = models.CharField(_("menu title"), max_length=255, unique=True, db_index=True)
    links = PlaceholderField("custom link block", help_text=_("Add links, e-mails, snippets to the menu."))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _("Custom Menu")
        verbose_name_plural = _("Custom Menus")
reversion_register(LinkBlock)


class AbstractMenuPlugin(CMSPlugin):
    """
        An abstract base class for the menu plugin classes
    """
    collapse = models.BooleanField(_("collapse menu"), default=False, help_text="Select this option if the menu should initially appear collapsed.")

    class Meta:
        abstract = True

class LinkBlockPtr(AbstractMenuPlugin):
    """
      Plugin model for a Custom Menu (Link Block)
    """
    link_block = models.ForeignKey(LinkBlock)

    class Meta:
        verbose_name = _("Custom Menu Plugin Model")

    def __unicode__(self):
        return self.link_block.name
reversion_register(LinkBlockPtr)


class NavMenu(AbstractMenuPlugin):
    """
       Plugin model for a sub-section navigation menu
    """
    title = models.CharField(_("menu title"), max_length=255, unique=True, db_index=True)
    section = models.ForeignKey(Page, blank=True, null=True, help_text=_("Defaults to the root of current page if left blank."))

    class Meta:
        verbose_name = _("Section Nav. Menu")

    def __unicode__(self):
        return self.title
reversion_register(NavMenu)
