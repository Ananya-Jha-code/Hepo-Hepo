from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput
    (attrs={'placeholder': 'Enter A Username...'}))

    email = forms.CharField(max_length=30, required=True, widget=forms.EmailInput
    (attrs={'placeholder':'Enter Your Email'}))

    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput
    (attrs={'placeholder': 'Enter Your Password'}))

    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput
    (attrs={'placeholder': 'Enter Password Again'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
