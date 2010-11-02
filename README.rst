==============================
Django CMS Menus Plugin
==============================

The Menus plugins are a collection of pluggable menus for `Django CMS <http://www.django-cms.org/>`_.

Current release is ALPHA.  Some limited testing has been done.  Please let me know if you use this module and how it works for you.

Menu types include:

* Custom Menu (Link Block): a re-usable, named block of links and/or snippets.  Useful, for example, for a "Quick Links" block, or other block of links that will be re-used on multiple pages on the site.
* Section Navigation Menu: display hierarchical navigation (nested lists) for all nodes below a given "root" 
  (any page on site - usually a section page with a child tree).  Useful for adding custom navigation blocks.
* Sitemap: simply a complete hierarchical navigation (nested lists) of all pages on the site.
 
Features
========

* Custom Menu: users add links, snippets, or other plugins (set in settings) to placeholder.
  Custom Menu's are re-usable so the same menu can be placed on several pages.
* Nav. Menu: user can select which sub-section of site to create menu for, or use current page's root by default.
* Both menus have a "collapse" option, which, if selected, adds class="collapse" to the menu so it can be collapsed using CSS or JS.
* Sitemap: template logic only plugin - simply renders show_menu tag.
* Easy to override templates and media - default CSS with collapse/expand logic included.
* Can use each plugin independently

Dependencies
============

None (other than django-cms itself)

License
=======
GNU General Public License - see `LICENSE <http://github.com/powderflask/cmsplugin-menus/blob/master/LICENSE>`_

You are free to copy, use, or modify this software in any way you like, but please provide attribution to the original author with a link to:
http://github.com/powderflask/cmsplugin-menus

Author
------
`Driftwood Cove Designs <http://designs.driftwoodcove.ca>`_

Installation
============

From PyPI
---------

not yet - sorry.

Manual Download
---------------

You can download a zipped archive from http://github.com/powderflask/cmsplugin-menus/downloads.

Unzip the file you downloaded. Then go in your terminal and ``cd`` into the unpacked folder. Then type ``python setup.py install`` in your terminal.

Configuration
-------------
Add one or more cmsplugin_menu plugins to your ``INSTALLED_APPS`` in settings.py:

INSTALLED_APPS = (..., 
                  cmsplugin_menus.plugins.*,  # installs all menu plugins
                 )  

OR  pick and choose:

INSTALLED_APPS = (...,
                  cmsplugin_menus.plugins.linkblock,
                  cmsplugin_menus.plugins.navigation,
                  cmsplugin_menus.plugins.sitemap,
                 )
                 
Don't forget to syncdb.

Media
-----
Media files for the plugins are expected at: {{ MEDIA_URL }}cmsplugin_menus/

In your MEDIA_ROOT, copy or link the cmsplugin_menus media: 

* ln -s /path/to/cmsplugin_menus/media/cmsplugin_menus

If you want to use the default CSS, which provides basic styles and expand/collapse logic,
include a link to the css file in your base template (or whichever template will have the menu plugins on them):

* <link rel="stylesheet" type="text/css" href='{{ MEDIA_URL }}cmsplugin_menus/css/cmsplugin_menu.css' 'media="all" />


Settings
========

No settings are required, however, some default settings can be overridden:

* CMSPLUGIN_MENUS_TEXT_ENABLED = False by default.  Set to True if menus should be available as text plugin.

* CMSPLUGIN_MENUS_PLACEHOLDER_CONF  Limits which plugins are allowed within a Custom Menu (link block)

You can override this setting to change the defaults (LinkPlugin and SnippetPlugin) in your settings like this:

CMSPLUGIN_MENUS_PLACEHOLDER_CONF = {
        'cmsplugin_menus link block': {
                'plugins': ('LinkPlugin', 'SnippetPlugin', ...),
                'name': gettext("links")
}}

OR 

CMSPLUGIN_MENUS_PLACEHOLDER_CONF = None  # don't limit plugin types in link blocks

OR  add the 'cmsplugin_menus link block' entry directly:

CMS_PLACEHOLDER_CONF = { ..., 'cmsplugin_menus link block': { ... }, ... }

Kudos
=====

* icons from the fabulous famfamfam silk icon set: http://www.famfamfam.com/lab/icons/silk/
