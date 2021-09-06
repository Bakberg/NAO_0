from django.contrib import admin
from .models import *

class DROPDOWN_ONEAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pblished',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')


admin.site.register(Dropdown_one, DROPDOWN_ONEAdmin)

class DROPDOWN_TWOAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pblished',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')


admin.site.register(Dropdown_two, DROPDOWN_TWOAdmin)

class DROPDOWN_THREEAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pblished',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')


admin.site.register(Dropdown_three, DROPDOWN_THREEAdmin)

class DROPDOWN_FORAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pblished',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'task')


admin.site.register(Dropdown_for, DROPDOWN_FORAdmin)
