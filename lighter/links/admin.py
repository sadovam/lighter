from django.contrib import admin

from .models import LinkGroup, LinkPage, Link

admin.site.register((LinkPage, LinkGroup, Link))
