from django.urls import path
from . import views

urlpatterns = [
    path('user-list/', views.user_list, name='user_list'),
    path('user-list2/', views.UserList2.as_view(), name='user_list2'),
]
