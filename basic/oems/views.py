from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def list(request):
    return HttpResponse('The number of employees have 25')
