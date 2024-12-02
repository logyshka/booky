from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    fullname = models.CharField(max_length=255, verbose_name='ФИО автора', unique=True)

    def __str__(self):
        return self.fullname
