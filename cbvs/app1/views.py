from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views import generic, View


def user_list(mmm):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(mmm, 'app1/user_list.html', context=context)


class UserList2(View):
    # model = User

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'app1/user_list.html', context=context)

    def post(self, request):
        return HttpResponse("POST")


class UserList3(generic.base.TemplateView):
    template_name = 'app1/user_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['users'] = User.objects.all()
    #     return context

    extra_context = {'users': User.objects.all()}


class GroupList(generic.ListView):
    model = Group
    test = 'test'


