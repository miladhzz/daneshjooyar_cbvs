from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Group
from django.views import generic, View


class UserList3(generic.base.TemplateView):
    template_name = 'app1/user_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['users'] = User.objects.all()
    #     return context

    extra_context = {'users': User.objects.all()}


class GroupList(generic.ListView):
    model = Group
    paginate_by = 2
    # allow_empty = False
    # queryset = Group.objects.filter(name__startswith="My11")

    def get_queryset(self):
        return Group.objects.filter(name__startswith="My")


class GroupDetail(generic.DetailView):
    model = Group
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        groupname = self.kwargs.get('groupname')
        return get_object_or_404(Group, id=id, name=groupname)


