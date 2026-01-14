from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Namangan1")
def index2(request):
    return HttpResponse("Namangan2")
# Create your views here.
