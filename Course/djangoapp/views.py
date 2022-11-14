from django.shortcuts import render
from datetime import datetime
# Create your views here.
'''
#Method 1
def learn_django(request):
    return render(request, 'courseinfo.html', {'name':'Django Framework'})

x
#Method 2
def learn_django(request):
    cname = 'Django'
    duration = '4 Months'
    seats = 10
    django_details = {'name':cname, 'du':duration, 'st':seats}
    return render(request, 'courseinfo.html', django_details)


#Method 3
def learn_django(request):
    return render(request, 'courseinfo.html', {'name':'Django is awesome'})

#Method 4
def learn_django(request):
    d = datetime.now()
    return render(request, 'courseinfo.html', {'dt':d})


#Method 5
def learn_django(request):
    return render(request, 'courseinfo.html', {'p1':56.24321, 'p2':56.000, 'p3':56.37000})


#Method 6
def learn_django(request):
    return render(request, 'courseinfo.html', {'name':True})

'''

#Method 7
def learn_django(request):
    return render(request, 'courseinfo.html', {'name':'Django', 'seat':5})



'''
#Method 9
def learn_django(request):
    student = {'names': ['Rahul', 'Sonam', 'Raj','Anu']}
    return render(request, 'courseinfo.html', student)

#Method 10
def learn_django(request):
    stu = {'stu1': {'name': 'Rahul', 'roll':101},
            'stu2': {'name': 'Sonam', 'roll':102},
            'stu3': {'name': 'Raj', 'roll':103},
            'stu4': {'name': 'Anu', 'roll':104},
          }
    students = {'student':stu}
    return render(request, 'courseinfo.html', students)

#Method 11
def learn_django(request):
    data = {'name': 'Rahul', 'roll':101}
    return render(request, 'courseinfo.html', {'data':data})

#Method 12
def learn_django(request):
    data = {'stu1': {'name': 'Rahul', 'roll':101},
              'stu2': {'name': 'Sonam', 'roll':102},
              'stu3': {'name': 'Raj', 'roll':103},
              'stu4': {'name': 'Anu', 'roll':104},
            }
    return render(request, 'courseinfo.html', {'data':data})
'''