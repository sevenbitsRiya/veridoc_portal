from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings

from .forms import SignUpForm,LoginForm
from .tokens import account_activation_token

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
#from settings import DEFAULT_FROM_EMAIL
from django.views.generic import *
from utils.forms.reset_password_form import PasswordResetRequestForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models.query_utils import Q

@login_required
def home(request):
    return render(request, 'accounts/home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_login(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'accounts/login.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            from_email = settings.EMAIL_HOST_USER
            to_email = form.cleaned_data.get('username')
            email = EmailMessage(
                        subject, message,from_email, to=[to_email]
            )
            email.send()
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'accounts/account_activation_invalid.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeRequestForm(request.POST)
        if form.is_valid():
            newpassword=form.cleaned_data['newpassword1'],
            username=request.user.username
            password=request.user.password

            user = authenticate(username=username, password=password)
            if user is not None:
                user.set_password(newpassword)
                user.save()
                return HttpResponseRedirect('/reset/success/')

            else:
                return render(request, 'reset_password.html',{'error':'You have entered wrong old password','form': form})

        else:
           return render(request, 'reset_password.html',{'error':'You have entered old password','form': form})
    else:
        form = PasswordChangeRequestForm()
    content = RequestContext(request, {'form': form})  
    return render(request, 'reset_password.html', content,)

class ResetPasswordRequestView(FormView):
        template_name = "account/test_template.html"    #code for template is given below the view's code
        success_url = '/account/login'
        form_class = PasswordResetRequestForm

        @staticmethod
        def validate_email_address(email):
            try:
                validate_email(email)
                return True
            except ValidationError:
                return False

        def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST)
            if form.is_valid():
                data= form.cleaned_data["email_or_username"]
            if self.validate_email_address(data) is True:                 #uses the method written above
                '''
                If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
                '''
                associated_users= User.objects.filter(Q(email=data)|Q(username=data))
                if associated_users.exists():
                    for user in associated_users:
                            c = {
                                'email': user.email,
                                'domain': request.META['HTTP_HOST'],
                                'site_name': 'your site',
                                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                'user': user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                                }
                            subject_template_name='registration/password_reset_subject.txt' 
                            # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                            email_template_name='registration/password_reset_email.html'    
                            # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                            subject = loader.render_to_string(subject_template_name, c)
                            # Email subject *must not* contain newlines
                            subject = ''.join(subject.splitlines())
                            email = loader.render_to_string(email_template_name, c)
                            send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                    result = self.form_valid(form)
                    messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                    return result
                result = self.form_invalid(form)
                messages.error(request, 'No user is associated with this email address')
                return result
            else:
                '''
                If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
                '''
                associated_users= User.objects.filter(username=data)
                if associated_users.exists():
                    for user in associated_users:
                        c = {
                            'email': user.email,
                            'domain': 'example.com', #or your domain
                            'site_name': 'example',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                            }
                        subject_template_name='registration/password_reset_subject.txt'
                        email_template_name='registration/password_reset_email.html'
                        subject = loader.render_to_string(subject_template_name, c)
                        # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                    result = self.form_valid(form)
                    messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
                    return result
                result = self.form_invalid(form)
                messages.error(request, 'This username does not exist in the system.')
                return result
            messages.error(request, 'Invalid Input')
            return self.form_invalid(form)