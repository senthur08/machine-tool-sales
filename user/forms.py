from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address= forms.CharField(max_length=255, required=True)

    class Meta:
        model= User
        fields = ['username', 'password1', 'password2']