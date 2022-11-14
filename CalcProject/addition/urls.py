from django.urls import path
from . import views

urlpatterns = [
    path("",views.add),
    # path("addition/",views.adding,),
    # path("substraction/",views.substract ),
    path("result/",views.result), 
]
