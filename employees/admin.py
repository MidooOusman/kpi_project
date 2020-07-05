from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','titel','is_published','state','list_date','manager')
    list_display_links = ('id','titel')
    list_filter = ('manager',)
    list_editable = ('is_published',)
    search_fields= ('id','titel','is_published','state','list_date','manager')
    list_per_page= 25
admin.site.register(Employee, EmployeeAdmin)
