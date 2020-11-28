from django.urls import path
from . import views
from django.views.generic import ListView
from django.contrib.auth.models import Group

urlpatterns = [
    path('user-list/', views.user_list, name='user_list'),
    path('user-list2/', views.UserList2.as_view(), name='user_list2'),
    path('group-list/', ListView.as_view(model=Group, context_object_name='groups'), name='group_list'),
    path('group-list2/', views.GroupList.as_view(context_object_name='groups', test='test2'), name='group_list2'),
    path('user-list3/', views.UserList3.as_view(), name='user_list3'),
]
