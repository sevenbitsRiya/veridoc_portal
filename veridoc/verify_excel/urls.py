from django.urls import path
from django.conf.urls import url, include

from .views import VDG_M_ExcelDetailsView


app_name = "verify_excel"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    #url(r'^verify_doc/(?P<apikey>\d+)/$', VDG_M_documentDetailsView.as_view(), name='verify_doc')
    path('doc', VDG_M_ExcelDetailsView.as_view(),name = 'doc'),
    
]