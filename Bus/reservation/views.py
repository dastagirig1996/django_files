from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def available(request):
    return HttpResponse("slleper :3,seating :2")

def book_tickets(request):
    s = 'seat no 06,07'
    t = 'type sleeper'
    return HttpResponse(s+' '+t)
    
def status(request):
    return HttpResponse('Your booking seat No 06,07 is conformed')
