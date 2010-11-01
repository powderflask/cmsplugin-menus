from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import LinkBlock

# Classes with placeholders must register with PlaceholderAdmin
admin.site.register(LinkBlock, PlaceholderAdmin)
