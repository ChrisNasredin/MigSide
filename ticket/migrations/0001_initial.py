# Generated by Django 4.2.4 on 2023-08-04 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_alter_employerposition_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Priorities',
                'db_table': 'priorities',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=256, verbose_name='Ticket Title')),
                ('desc', models.CharField(max_length=256, verbose_name='Ticket Description')),
                ('deadline_date', models.DateTimeField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_tickets', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('execution_department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='account.employerposition', verbose_name='Execution Department')),
                ('executor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='Executor')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticket.priority', verbose_name='Priority')),
            ],
            options={
                'verbose_name': 'Tiket',
                'verbose_name_plural': 'Tickets',
                'db_table': 'tickets',
            },
        ),
    ]