from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='personne'),
    path('', views.index, name='adduser'),
]