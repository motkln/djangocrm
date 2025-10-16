from django.db import models
from django.conf import settings


class Company(models.Model):
    inn = models.CharField(verbose_name='ИНН', max_length=12, unique=True)
    title = models.CharField(verbose_name='Название компании', max_length=256)

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_company',
        verbose_name='Владелец'
    )

    def __str__(self):
        return self.title

