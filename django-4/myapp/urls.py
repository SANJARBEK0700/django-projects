from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
]
