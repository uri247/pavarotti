from django.contrib import admin
from faves.models import Link, LinkGroup


class LinkInline(admin.TabularInline):
    model = Link
    extra = 5

class LinkGroupAdmin(admin.ModelAdmin):
    fields = ['title', 'created_date']
    inlines = [LinkInline]
    list_display = ['title', 'created_date', 'is_recent']
    list_filter = ['created_date']

    

admin.site.register(Link)
admin.site.register(LinkGroup, LinkGroupAdmin)

