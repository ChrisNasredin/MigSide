from django.forms import ModelForm, DateTimeInput
from .utils import DateTimePickerInput, ColorPickerInput

from .models import Ticket, Priority


class CreateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'desc', 'executor', 'execution_department', 'deadline_date', 'priority']
        widgets = {'deadline_date': DateTimePickerInput()}


class AdminPriorityForm(ModelForm):
    class Meta:
        model = Priority
        widgets = {'color': ColorPickerInput()}
        fields = '__all__'
