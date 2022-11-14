from django.shortcuts import render
from .models import student
# Create your views here.
def details(request):
    stu = student.objects.all()
    return render(request,'home.html',{'s':stu})