from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def theory(request):
    return HttpResponse('<i>Telugu, Hindhi, English </i>')
def practical(request):
    return HttpResponse('<i> science, social, mathematics</i>')