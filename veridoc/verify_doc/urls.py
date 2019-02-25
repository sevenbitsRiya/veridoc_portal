from django.urls import path
from django.conf.urls import url, include

from .views import VDG_M_documentDetailsView


app_name = "verify_doc"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    #url(r'^verify_doc/(?P<apikey>\d+)/$', VDG_M_documentDetailsView.as_view(), name='verify_doc')
    path('verify_doc/', VDG_M_documentDetailsView.as_view()),
    
]