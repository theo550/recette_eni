from django.urls import path

from ReciepApp import views

urlpatterns = [
    path('recipes', views.recipes),
    path('recipes/<int:id>', views.recipe),
]
