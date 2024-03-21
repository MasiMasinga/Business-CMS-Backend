from django.contrib import admin
from .models import Department, Role, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]

class RoleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Role._meta.fields]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
