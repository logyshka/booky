from django.db import models


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    name = models.CharField(max_length=100, verbose_name='Название контакта')
    value = models.CharField(max_length=100, verbose_name='Значение для контакта')

    def __str__(self):
        return self.name
