"""basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from oilc import views as v1
from oems import views as v2

from oilc.views import message,home,greeting
from oems.views import list

from anil import views
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('message',views.message),
#     path('',views.home),
#     path('greeting/',views.greeting),
#     # path('list/',views.list),
# ]


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('message',v1.message),
#     path('',v1.home),
#     path('greeting/',v1.greeting),
#     path('list/',v2.list),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path('message',message),
    path('',home),
    path('greeting/',greeting),
    path('list/',list),
    path("h/",include('anil.urls'))

]
