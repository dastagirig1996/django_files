from django.shortcuts import render
#from django.http import HttpResponse


def add(request):
    return render(request,'add.html')

def result(request):

    try:

        if 'Add' in request.GET:
            a = int(request.GET['n1'])
            b = int(request.GET['n2'])

            ad = a+b
            #return HttpResponse(ad)
            return render(request, 'add.html',{'ad':ad})


        elif 'Sub' in request.GET:
            a = int(request.GET['n1'])
            b = int(request.GET['n2'])

            su = a-b
            return render(request, 'add.html',{'su':su})

        elif 'Mul' in request.GET:
            a = int(request.GET['n1'])
            b = int(request.GET['n2'])

            mu = a*b
            return render(request, 'add.html',{'mu':mu})

        elif 'Div' in request.GET:
            a = int(request.GET['n1'])
            b = int(request.GET['n2'])

            di = a/b
            return render(request, 'add.html',{'di':di})
    except:

        return render(request, 'add.html', {'c': 'Enter numbers only'})

    
    





    #except:
        # print("Invalid inputs...")
        # return render(request, 'addition.html', {'ad': 'required all fields'})
    