from django.urls import path, include
from .views.auth.register_view import RegisterView
from .views.auth.login_view import LoginView
from .views.protected_view import ProtectedView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('protected/', ProtectedView.as_view()),
    path('', include('src.interfaces.api.views.student.urls')),
    path('', include('src.interfaces.api.views.professor.urls')),
    path('', include('src.interfaces.api.views.discipline.urls')),
    path('', include('src.interfaces.api.views.room.urls')),
    path('', include('src.interfaces.api.views.class_session.urls')),
]