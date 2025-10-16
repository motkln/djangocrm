from django.db import models
from django.conf import settings
from companies.models import Company

class Storage(models.Model):
    company = models.OneToOneField(
        Company,
        on_delete=models.SET_NULL,
        related_name='storages',
        verbose_name='Склад компании',
        null=True
    )
    address = models.CharField(verbose_name='Адрес', max_length=50, unique=False)
    title = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return f"Склад {self.company.title} — {self.address}"
