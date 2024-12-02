from django.db import models


class Message(models.Model):
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    user = models.ForeignKey(
        to='auth.User',
        related_name='messages',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    book = models.ForeignKey(
        to='Book',
        related_name='messages',
        on_delete=models.CASCADE,
        verbose_name='Книга'
    )
    text = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
