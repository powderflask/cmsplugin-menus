from models import LinkBlock, NavMenu
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin

admin.site.register(NavMenu, admin.ModelAdmin)

# Classes with placeholders must register with PlaceholderAdmin
admin.site.register(LinkBlock, PlaceholderAdmin)
