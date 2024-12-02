from django import forms
from django.core.exceptions import ValidationError

from ..models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ("rating",)

    def __init__(self, user, book, *args, **kwargs):
        self.user = user
        self.book = book
        super(RatingForm, self).__init__(*args, **kwargs)
        rating_value = Rating.objects.filter(user=user, book=book).first()
        self.current_rating = rating_value.rating if rating_value else None
        self.fields['rating'].widget = forms.NumberInput(attrs={
            'min': 1,
            'max': 10,
            'step': 1,
            'value': rating_value or 1
        })

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if 1 > rating > 10:
            raise ValidationError('Рейтинг не может быть меньше 1 или больше 10')

        return rating

    def save(self, commit=True):
        rating = super().save(commit=False)  # Не сохраняем сразу в базу
        rating.user = self.user
        rating.book = self.book
        if commit:
            rating.save()
        return rating
