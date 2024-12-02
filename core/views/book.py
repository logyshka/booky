from django import views
from django.db.models import Q

from ..forms.rating import RatingForm
from ..models import Book, Rating


class BookListView(views.generic.ListView):
    template_name = 'core/book-list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        context['selected_genres'] = self.request.GET.getlist('genres')
        page_obj = context['page_obj']
        context['next_page'] = page_obj.number + 1 if page_obj.has_next() else None
        context['prev_page'] = page_obj.number - 1 if page_obj.has_previous() else None
        print(context)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        genres = self.request.GET.getlist('genres')  # Список выбранных жанров

        if query:
            queryset = queryset.filter(
                Q(title__contains=query) | Q(author__fullname__contains=query)
            )

        if genres:
            queryset = queryset.filter(genres__id__in=genres).distinct()

        return queryset


class BookDetailView(views.generic.DetailView):
    template_name = 'core/book-detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if user.is_authenticated:
            context['rating'] = Rating.objects.filter(book=self.object, user=user).first()
            context['rating_form'] = RatingForm(user=user, book=self.object)
        return context
