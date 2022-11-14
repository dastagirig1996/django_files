from django.urls import path, re_path
from . import views

urlpatterns = [
path('staff/',views.cheff),
#re_path(r'^.*$',views.supporting_cheff),
path('sp/',views.supporting_cheff),
]