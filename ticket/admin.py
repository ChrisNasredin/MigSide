from django.contrib import admin
from .models import Priority, Ticket
from .forms import AdminPriorityForm
from django.utils.html import mark_safe


# Register your models here.

class PriorityAdmin(admin.ModelAdmin):
    form = AdminPriorityForm
    list_display = ['id', 'name', 'color_view']

    def color_view(self, obj):
        return mark_safe(f'<div style="background-color: {obj.color}; width: 50px; height: 15px;"></div>')


class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'executor', 'execution_department', 'deadline_date']


admin.site.register(Priority, PriorityAdmin)
admin.site.register(Ticket, TicketAdmin)
