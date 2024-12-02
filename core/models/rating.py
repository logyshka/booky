from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Rating(models.Model):
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = (('book', 'user'),)

    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
        verbose_name='Книга',
        related_name='ratings'
    )
    user = models.ForeignKey(
        to='auth.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='ratings'
    )
    rating = models.IntegerField(verbose_name='Рейтинг')

    def __str__(self):
        return str(self.rating)


@receiver(post_save, sender=Rating)
def update_book_rating_on_save(sender, instance, **kwargs):
    update_book_rating(instance.book)


@receiver(post_delete, sender=Rating)
def update_book_rating_on_delete(sender, instance, **kwargs):
    update_book_rating(instance.book)


def update_book_rating(book):
    avg_rating = book.ratings.aggregate(average=Avg('rating'))['average'] or 0.0
    book.rating = avg_rating
    book.save()
