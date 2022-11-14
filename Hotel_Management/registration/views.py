from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def available(request):
    return HttpResponse("<h2> 40 rooms available for  booking </h2>")

def booked(request):
    return HttpResponse('<center> booking conformed customers 15 </center>')

