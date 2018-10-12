from django.urls import path

from . import views

urlpatterns = [
    path('', views.color_generation, name = 'table')
]
