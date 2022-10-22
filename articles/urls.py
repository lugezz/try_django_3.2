from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_search_view),
    path('create/', views.article_create),
    path('<int:id_art>/', views.article_view),
]
