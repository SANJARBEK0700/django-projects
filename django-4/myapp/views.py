from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("First-app")
def index2(request):
    return HttpResponse("Second-app")
# Create your views here.
