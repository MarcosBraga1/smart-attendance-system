import allauth
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('src.interfaces.api.urls')),
    path('accounts/', include('allauth.urls')),
]
