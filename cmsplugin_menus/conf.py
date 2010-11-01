
ALREADY_PATCHED = False

def patch_settings():
    """
    Merge settings with default menus settings, so all required attributes
    will exist. Never override, just append any unspecified settings.
    """
    global ALREADY_PATCHED
    
    # do this just once
    if ALREADY_PATCHED:
        return
    
    ALREADY_PATCHED = True
    
    from django.conf import settings  # load project settings (overrides)
    import default_settings
    import constants
    
    # merge with default menus settings
    for attr in dir(default_settings):
        if attr == attr.upper() and not hasattr(settings, attr):
            setattr(settings._wrapped, attr, getattr(default_settings, attr))

    # Limit plugins in Link Blocks (unless overridden)
    if constants.CMSPLUGIN_MENUS_LINK_BLOCK_PLACEHOLDER not in settings.CMS_PLACEHOLDER_CONF \
        and settings.CMSPLUGIN_MENUS_PLACEHOLDER_CONF:
        settings.CMS_PLACEHOLDER_CONF.update(settings.CMSPLUGIN_MENUS_PLACEHOLDER_CONF)
        