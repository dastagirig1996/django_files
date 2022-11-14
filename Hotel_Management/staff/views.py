from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cheff(request):
    return HttpResponse("Total chefs are 12")

def supporting_cheff(request):
    return HttpResponse('the total supporting staff were 26')