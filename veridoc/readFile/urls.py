from django.urls import path
from django.conf.urls import url, include

from .views import VDG_M_readFileView


app_name = "readFile"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('readfile', VDG_M_readFileView.as_view(),name = 'readfile'),
   
]