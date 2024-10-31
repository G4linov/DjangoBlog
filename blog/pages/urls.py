from django.urls import path

from . import views

from django.urls import path

urlpatterns = [
    path('about/', views.about),
    path('rules/', views.rules),
]