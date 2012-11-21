__author__ = 'student1'
from wikicamp.wiki.models import Page
from django.contrib import admin

class PageInline(admin.TabularInline):
    model = Page
    extra = 3

class WikiAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['content']})
    ]
#    inlines = [PageInline]

admin.site.register(Page, WikiAdmin)