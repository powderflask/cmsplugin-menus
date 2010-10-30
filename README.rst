==============================
Django CMS Menus Plugin
==============================

The Menus plugins are a collection of pluggable menus for `Django CMS <http://www.django-cms.org/>`_.

Currently this plugin is in development - NOT FOR USE ON PRODUCTION SITES!

Menu types include:

* Custom Menu (Link Block): a re-usable, named block of links and/or snippets.  Useful, for example, for a "Quick Links" block, or other block of links that will be re-used on multiple pages on the site.
* Section Navigation Menu: display complete, hierarchical navigation (nested lists) for all nodes below a given "root" 
(any page on site - usually a section page with a child tree).  Useful for adding custom custom navigation blocks.

Features
========

* Link block is simply a model with a name and placeholder - users add links, snippets, or other plugins (set in settings) 
* Nav. Menu 
* Both menus have a "collapse" option, which, if selected, adds class="collapse" to the menu so it can be collapsed using JS.
* JQuery script for handling collapse/expand logic is included

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

You can download a zipped archive from http://github.com/powderflask/cmsplugin-menus/downloadss.

Unzip the file you downloaded. Then go in your terminal and ``cd`` into the unpacked folder. Then type ``python setup.py install`` in your terminal.

Put "cmsplugin_menu" in your ``INSTALLED_APPS`` section in settings.py. Don't forget to syncdb your database.

Settings
========

No settings are required, however, some default settings can be overridden:

* CMSPLUGIN_MENUS_TEXT_ENABLED = False by default.  Set to True if menus should be available as text plugin.

* CMS_PLACEHODER_CONF  Limits which plugins are allowed within a Custom Menu (link block)
You can overide this setting to change the defaults (LinkPlugin and SnippetPlugin) in your settings like this:

CMS_PLACEHOLDER_CONF = {
    ...
    'link-block': {
            'plugins': ('LinkPlugin', 'SnippetPlugin', ...),
            'name': gettext("Link Block")
}}
