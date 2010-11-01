from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.utils.helpers import reversion_register
from cmsplugin_menus import constants
from cmsplugin_menus.models import LinkBlock


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
