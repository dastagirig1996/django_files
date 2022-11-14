from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def message(request):
    return HttpResponse("Hello world")

def home(request):
    h = 'This is Home Page'
    return HttpResponse(h)

def greeting(request):
    return HttpResponse('<H1>Good Morning</H1>')