from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page
from cms.utils.helpers import reversion_register

class NavMenu(CMSPlugin):
    """
       Plugin model for a sub-section navigation menu
    """
    title = models.CharField(_("menu title"), max_length=255, blank=True, default="", help_text=_("Defaults to section page title if left blank."))
    section = models.ForeignKey(Page, blank=True, null=True, help_text=_("Defaults to the root of current page if left blank."))
    collapse = models.BooleanField(_("collapse menu"), default=False, help_text="Select this option if the menu should initially appear collapsed.")

    class Meta:
        verbose_name = _("Section Nav. Menu")

    def __unicode__(self):
        return self.title
reversion_register(NavMenu)
