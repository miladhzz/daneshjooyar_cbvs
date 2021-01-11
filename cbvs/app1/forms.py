from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    password2 = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('groups', 'first_name', )

    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
