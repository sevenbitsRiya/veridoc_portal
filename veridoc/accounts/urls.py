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
from . import views



urlpatterns = [
    url(r'^$', l_views.home, name='home'),
    url(r'^user_login/$',l_views.user_login,name='user_login'),
    url(r'^user_logout/$', l_views.user_logout, name='user_logout'),
    url(r'^signup/$', l_views.signup, name='signup'),
    url(r'^account_activation_sent/$', l_views.account_activation_sent, name='account_activation_sent'),
        url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        l_views.activate, name='activate'),
    url(r'^password/$', views.change_password, name='change_password'),

    
    #url(r'^accounts/password/reset/done/$',
     #   PasswordResetView.as_view(),
     #  {'template_name': 'accounts/password_reset_done.html'},
     #  name="password_reset_done"),
    # new url definitions
    #url(r'^accounts/password/change/$', password_change, {
    #    'template_name': 'accounts/password_change_form.html'}, 
     #   name='password_change'),
    #url(r'^accounts/password/change/done/$', password_change_done, 
     #   {'template_name': 'accounts/password_change_done.html'},
      #  name='password_change_done'),'''
    
    
    #url(r'^change_password/$',l_views.change_password, name='change_password'),
    #url("^password_chnage/$",l_views.password_change,name="password_reset"),
    #path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name='password_reset_complete'),
    #url(r'^password_reset/$',views.PasswordResetView.as_view(
     #   template_name="accounts/password_reset_form.html",
     #   email_template_name="accounts/password_reset_email.html",
     #   success_url=reverse_lazy('accounts/password_reset_done'), # might be required
    #),
    #name='password_reset'
#),
]