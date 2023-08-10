from django.forms import DateTimeInput, TextInput


class DateTimePickerInput(DateTimeInput):
    input_type = 'date'


class ColorPickerInput(TextInput):
    input_type = 'color'
