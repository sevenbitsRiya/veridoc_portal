from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    email = forms.EmailField(
    widget=forms.HiddenInput(),
    required = False,
    initial="dummy@freestuff.com"
)   

    def save(self, commit=True):
        user = super().save(commit=False) # here the object is not commited in db
        user.email = self.cleaned_data['username']
        user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'password1', 'password2')

class LoginForm(UserCreationForm):
    username = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','password')

class PasswordChangeRequestForm(UserCreationForm):
    pass

