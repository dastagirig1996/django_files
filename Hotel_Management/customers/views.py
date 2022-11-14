from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def total(request):
    return HttpResponse("Toatal customers 50")
def filled(request):
    return HttpResponse("Total 20 rooms fillled")