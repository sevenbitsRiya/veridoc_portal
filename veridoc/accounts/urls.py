from django.conf.urls import url, include
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login, logout
#from veridoc.accounts import views as core_views
from . import views as l_views
#from django.contrib.auth.views import (
#   PasswordResetView,
#    PasswordResetDoneView,
#    PasswordResetConfirmView,
 #   PasswordResetCompleteView
#)
#from django.contrib.auth import views as auth_views
from django.contrib.auth import views 
from django.urls import reverse_lazy

from django.urls import path
from . import views as l_views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns = [
    url(r'^$', l_views.home, name='home'),
    url(r'^user_login/$',l_views.user_login,name='user_login'),
    url(r'^user_logout/$', l_views.user_logout, name='user_logout'),
    url(r'^signup/$', l_views.signup, name='signup'),
    url(r'^account_activation_sent/$', l_views.account_activation_sent, name='account_activation_sent'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        l_views.activate, name='activate'),
    url('^password/$', include('django.contrib.auth.urls')),
]