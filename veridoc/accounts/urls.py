from django.conf.urls import url, include
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import login, logout
#from veridoc.accounts import views as core_views
from . import views
from django.contrib.auth.views import (
   PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^change_password/$', views.change_password, name='change_password'),

    url(r'^password_reset/$',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'),    
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    #url(r'^accounts/reset_password', PasswordResetView.as_view(), name="reset_password"), 

]