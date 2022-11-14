from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    now = datetime.datetime.now()
    return render(request,'home.html',{'dt':now,'b':'mozila','v':10.0}, )

def show(request):
    return render(request,'show.html')

def super(request):
    return render(request,'blocksuper.html')