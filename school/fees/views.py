from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def total(request):
    total = '''for books = 15000.00
             for unoform = 1800.00
            for tution = 22000.00'''
    return HttpResponse('<h3> {} </h3>'.format(total))

def discount(request):
    return HttpResponse('Discount of 20%')