from django.contrib import admin
from faves.models import Link, LinkGroup


class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'group']}),
        ('History', {'fields': ['visited']}),
        ('Network', {'fields': ['url']}),
    ]
    

admin.site.register(Link, LinkAdmin)
admin.site.register(LinkGroup)
