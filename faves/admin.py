from django.contrib import admin
from faves.models import Link, LinkGroup


class LinkInline(admin.StackedInline):
    model = Link
    extra = 5

class LinkGroupAdmin(admin.ModelAdmin):
    fields = ['title', 'created_date']
    inlines = [LinkInline]


admin.site.register(LinkGroup, LinkGroupAdmin)

