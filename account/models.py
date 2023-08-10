from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    position = models.ForeignKey('EmployerPosition',
                                 on_delete=models.PROTECT,
                                 verbose_name='Должность',
                                 blank=True,
                                 null=True)
    
    class Meta:
        db_table = 'users'

class EmployerPosition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Отдел')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employer_positions'
