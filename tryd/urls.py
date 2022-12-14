from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls), 
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
