from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.category, name="category"),
    #path('search', views.search, name="search"),
]