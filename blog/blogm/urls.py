from django.urls import path

from . import views

from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.post_detail),
    path('<slug:category_slug>/', views.category_posts),
]