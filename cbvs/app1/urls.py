from django.urls import path
from . import views
from django.views.generic import ListView
from django.contrib.auth.models import Group

urlpatterns = [
    path('', views.UserList.as_view(), name="user_list"),
    path('register/', views.RegisterUser.as_view(), name="register_user"),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),

]
