from django.urls import path
from . import views
urlpatterns = [
    path("namangan/", views.index),
    path("namangan2/", views.index2),
]