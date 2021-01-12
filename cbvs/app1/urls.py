from django.urls import path
from . import views
from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path('', views.UserList.as_view(), name="user_list"),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('user-group-list/<str:group>/', views.UserGroupList.as_view(), name="user_group_list"),
    path('user-edit/<int:pk>/', views.UserEdit.as_view(), name="user_edit"),
    path('user-group-ajax/', views.UserGroupAjax.as_view(), name="user_group_ajax"),
    path('users-ajax/', views.UsersAjax.as_view(), name="users_ajax"),
]
