from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    password2 = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]

