from django.urls import path
from . import views
urlpatterns = [
    path("fergana/", views.index),
    path("fergana2/", views.index2),
]