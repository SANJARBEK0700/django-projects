from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Farg'ona1")
def index2(request):
    return HttpResponse("Farg'ona2")
# Create your views here.
