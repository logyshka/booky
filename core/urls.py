from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api import viewsets
from .views import *

api_router = DefaultRouter()
api_router.register(r'authors', viewsets.AuthorViewSet)
api_router.register(r'books', viewsets.BookViewSet)
api_router.register(r'genres', viewsets.GenreViewSet)
api_router.register(r'ratings', viewsets.RatingViewSet)
api_router.register(r'messages', viewsets.MessageViewSet)

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/<uuid:pk>/', BookDetailView.as_view(), name='book'),
    path('books/<uuid:book>/rating/', RatingUpdateOrCreateView.as_view(), name='rating'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('api/', include(api_router.urls), name='api'),
]
