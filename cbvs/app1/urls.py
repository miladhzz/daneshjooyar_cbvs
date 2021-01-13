from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.UserList.as_view(), name="user_list"),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('user-group-list/<str:group>/', views.UserGroupList.as_view(), name="user_group_list"),
    path('user-edit/<int:pk>/', views.UserEdit.as_view(), name="user_edit"),
    path('user-group-ajax/', views.UserGroupAjax.as_view(), name="user_group_ajax"),
    path('users-ajax/', views.UsersAjax.as_view(), name="users_ajax"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
