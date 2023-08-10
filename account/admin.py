from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmployerPosition


# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Кастомные параметры', {'fields': ('position',)}),
    )


class EmployerAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(EmployerPosition, EmployerAdmin)
