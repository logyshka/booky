import uuid

from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        unique_together = ('title', 'author')
        ordering = ('title',)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE, verbose_name='Автор', related_name='books')
    genres = models.ManyToManyField(to='Genre', verbose_name='Жанры', blank=True, related_name='books')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.title} | {self.author}'
