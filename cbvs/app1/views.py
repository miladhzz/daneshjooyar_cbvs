from django.contrib.auth.models import User, Group
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from . import forms
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from .mixins import JSONResponseMixin


class UserList(generic.ListView):
    model = User


class UserDetail(LoginRequiredMixin, generic.DetailView):
    model = User
    count = 0
    test = None

    def get_context_data(self, **kwargs):
        self.test = "test1"
        self.count += 1
        print("get_context_data", self.count)
        context = super(UserDetail, self).get_context_data(**kwargs)
        context["user_count"] = User.objects.count
        return context

    def get_object(self, queryset=None):
        self.count += 1
        print("get_object", self.count)
        user = super(UserDetail, self).get_object(queryset)
        user.last_login = timezone.now()
        user.save()
        return user

    def get(self, request, *args, **kwargs):
        self.count += 1
        print("get", self.count)
        return super(UserDetail, self).get(request, *args, **kwargs)

    def get_queryset(self):
        print(self.test)
        self.count += 1
        print("get_queryset", self.count)
        return super(UserDetail, self).get_queryset()


class UserGroupList(LoginRequiredMixin, generic.ListView):
    template_name = "auth/user_group_list.html"

    def get_queryset(self):
        self.group = Group.objects.get(name=self.kwargs["group"])
        return User.objects.filter(groups=self.group)

    def get_context_data(self, **kwargs):
        context = super(UserGroupList, self).get_context_data(**kwargs)
        context["group_name"] = self.group
        return context


@method_decorator(login_required, name="dispatch")
class UserEdit(generic.UpdateView):
    model = User
    form_class = forms.UserEditForm
    template_name = "app1/user-edit.html"

    # success_url = reverse_lazy('user_list')

    def get_success_url(self):
        return reverse('user_detail', args=[self.object.id])

    def form_valid(self, form):
        print("form_valid")
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        print("post")
        return super(UserEdit, self).post(request, *args, **kwargs)


class UserGroupAjax(LoginRequiredMixin, generic.TemplateView):
    template_name = "app1/user_group_ajax.html"

    def get_context_data(self, **kwargs):
        context = super(UserGroupAjax, self).get_context_data(**kwargs)
        context["groups"] = Group.objects.all()
        return context


class UsersAjax(JSONResponseMixin, LoginRequiredMixin, generic.View):

    def get(self, request):
        group_id = request.GET.get('group')
        users = User.objects.filter(groups=group_id).values('id', 'username')
        return self.render_to_json_response(users)
