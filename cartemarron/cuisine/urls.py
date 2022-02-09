"""Links URLs to corresponing views."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cookbook/', views.recipe_book, name='recipe_book'),
    path('cookbook/<int:recipe_id>/', views.recipe, name='recipe'),
]
