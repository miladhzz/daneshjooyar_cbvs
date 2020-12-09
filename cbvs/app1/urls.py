from django.urls import path
from . import views
from django.views.generic import ListView
from django.contrib.auth.models import Group

urlpatterns = [
    path('group-list2/', views.GroupList.as_view(), name='group_list2'),
    path('user-list3/', views.UserList3.as_view(), name='user_list3'),
    path('group-detail/<int:id>/<str:groupname>/', views.GroupDetail.as_view(), name='group_detail'),
    path('create-group/', views.CreateGroup.as_view(), name='create_group'),
]
