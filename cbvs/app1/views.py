from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views import generic


def user_list(mmm):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(mmm, 'app1/user_list.html', context=context)


class UserList2(generic.ListView):
    model = User


class GroupList(generic.ListView):
    model = Group
    test = 'test'


