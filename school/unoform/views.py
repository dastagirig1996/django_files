from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def color(request):
    c = 'blue color dress'
    return HttpResponse(c)

def pair(request):
    p = 'shirt, pant'
    return  HttpResponse(p)