from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def details(request):    
    return HttpResponse("<H1> Anil is good boy</H1>")