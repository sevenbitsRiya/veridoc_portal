from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #email = username
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(UserCreationForm):
    username = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','password')
class PasswordChangeRequestForm(UserCreationForm):
    pass
class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)