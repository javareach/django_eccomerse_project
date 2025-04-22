from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class Login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
      'placeholder':'Your username',
      'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
      'placeholder':'Enter your password',
      'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email',  'password1', 'password2', )

    # username = forms.CharField(widget=forms.TextInput(attrs={
    #   'placeholder':'Your username',
    #   'class': 'w-full py-4 px-6 rounded-xl'
    # }))

    # email = forms.EmailField(widget=forms.TextInput(attrs={
    #   'placeholder':'Your username',
    #   'class': 'w-full py-4 px-6 rounded-xl'
    # }))