from django.contrib import admin
from .models import *

class NEWAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pblished',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')

admin.site.register(New, NEWAdmin)

class LAST_NEWAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pblished',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')

admin.site.register(Last_new, LAST_NEWAdmin)