from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def verify(request,uniqeId):
    return HttpResponse("Hello user")