from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = "verify"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('<int:uniqeId>',views.verify),
    
]