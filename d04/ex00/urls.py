from django.urls import path

from . import views

urlpatterns = [
    path('', views.markdown_writer, name = 'contact')
]
