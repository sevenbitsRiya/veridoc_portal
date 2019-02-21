from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^get_api_key/$',views.get_api_key,name='get_api_key'),
]