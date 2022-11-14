from django.urls import path
from . import views
urlpatterns = [

    path('tt/',views.total),
    path('booked/',views.filled),
]