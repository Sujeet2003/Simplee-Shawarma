from django.urls import path
from Base import views

urlpatterns = [
    path('', views.index),
]