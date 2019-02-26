from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^key/$',views.key,name='key'),
]