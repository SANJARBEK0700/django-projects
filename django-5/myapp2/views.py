from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Toshkent1")
def index2(request):
    return HttpResponse("Toshkent2")
# Create your views here.
