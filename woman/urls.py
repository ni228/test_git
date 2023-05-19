from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('i/', views.index2, name='main2'),
    path('create/', views.create, name='create'),
]
