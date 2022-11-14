from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def route(request):
    return HttpResponse('<sup>from school to kphb</sup>')

def time(request):
    return HttpResponse('<sub> starts at 7am from Kphb& drops at 6pm </sub>')