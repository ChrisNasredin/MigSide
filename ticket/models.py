from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy


# Create your models here.

class Ticket(models.Model):


    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('account.User',
                               related_name='created_tickets',
                               on_delete=models.PROTECT,
                               verbose_name='Author')
    executors = models.ForeignKey('account.User',
                                 related_name='tickets',
                                 blank=True, null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name='Executor')
    execution_department = models.ForeignKey('account.EmployerPosition',
                                             blank=True, null=True,
                                             on_delete=models.PROTECT,
                                             verbose_name='Execution Department')
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name='Ticket Title')
    desc = models.CharField(max_length=256, verbose_name='Ticket Description')
    priority = models.ForeignKey('Priority',
                                 verbose_name='Priority',
                                 on_delete=models.PROTECT)
    deadline_date = models.DateTimeField(blank=True)
    ticket_date = models.DateTimeField(blank=True)
    done = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    periodic = models.BooleanField(default=False)
    repeat_period = models.DurationField(blank=True, null=True)


    def clean(self):
        if not (self.executor or self.execution_department):
            raise ValidationError('Executor or execution department must be choose')

    def get_absolute_url(self):
        return reverse_lazy('ticket:detail_ticket', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tickets'
        verbose_name = 'Tiket'
        verbose_name_plural = 'Tickets'


class Priority(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=7)

    def clean(self):
        # add regular exp validator for web-color
        pass

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'priorities'
        verbose_name = 'Priority'
        verbose_name_plural = 'Priorities'
