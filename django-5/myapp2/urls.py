from django.urls import path
from . import views
urlpatterns = [
    path('toshkent/', views.index),
    path('toshkent2/', views.index2),
]