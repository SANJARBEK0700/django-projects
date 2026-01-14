from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test_func(request):
    return HttpResponse('Bosh Sahifa')

def get_name(request):
    return HttpResponse('Javohir')