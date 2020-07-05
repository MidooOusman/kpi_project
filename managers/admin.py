from django.contrib import admin

from .models import Manager

class ManagerAdmin(admin.ModelAdmin):
    list_display= ('id', 'email','name','hire_date')
    list_display_links = ('id', 'email','name','hire_date')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Manager,ManagerAdmin)
