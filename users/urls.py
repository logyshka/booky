from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import UserRegisterView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("home")), name="logout"),
]
