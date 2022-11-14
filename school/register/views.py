from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add(request):
    return HttpResponse('kiran added successfully')
def show(request):
    return HttpResponse('Kiran exist in the list')
    