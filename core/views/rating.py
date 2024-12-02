from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from core.forms.rating import RatingForm
from core.models import Rating


class RatingUpdateOrCreateView(LoginRequiredMixin, FormView):
    http_method_names = ['post']
    form_class = RatingForm
    login_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['book'] = self.kwargs.get('book')
        return kwargs

    def get_success_url(self):
        return reverse('book', kwargs={'pk': self.kwargs.get('book')})

    def form_valid(self, form: RatingForm):
        rating = form.clean_rating()
        Rating.objects.update_or_create(user=form.user, book_id=form.book, defaults={'rating': rating})
        return super().form_valid(form)
