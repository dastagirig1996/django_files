from django.urls import path
from . import views
urlpatterns = [
    path('avail/',views.available),
    path('book/',views.booked)
]
