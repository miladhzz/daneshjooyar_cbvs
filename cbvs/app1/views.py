from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from . import forms
from django.contrib.auth.forms import UserCreationForm


class UserList(generic.ListView):
    model = User


class UserDetail(generic.DetailView):
    model = User


class RegisterUser(generic.CreateView):
    model = User
    # fields = ["username", "password", "first_name", "last_name"]
    form_class = forms.UserRegisterForm
    # success_url = reverse_lazy("user_list")

    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.set_password(form.cleaned_data["password"])
    #     user.save()
    #     return HttpResponseRedirect(reverse("user_detail", args=[user.id, ]))

    def get_success_url(self):
        return reverse("user_detail", args=[self.object.id, ])
