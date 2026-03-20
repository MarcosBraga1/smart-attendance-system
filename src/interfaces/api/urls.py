from django.urls import path
from .views.auth.register_view import RegisterView
from .views.auth.login_view import LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]