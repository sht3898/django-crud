from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:article_pk>/', views.detail),
    path('delete/', views.delete),
    path('one/', views.one),
    path('two/', views.two),
]