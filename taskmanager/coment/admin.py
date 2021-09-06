from django.contrib import admin
from .models import *

class COMENTAdmin(admin.ModelAdmin):
    list_display = ('title','task')
    search_fields = ('title', 'task')

admin.site.register(Coment, COMENTAdmin)

