from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#alt+enter 하면.... 뜸..

def hello_world(request):
    return HttpResponse('Hello World!')