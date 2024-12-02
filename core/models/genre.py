from django.db import models


class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(max_length=255, verbose_name='Жанр', unique=True)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Genre) and self.id == other.id
