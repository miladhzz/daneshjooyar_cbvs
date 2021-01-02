from django.urls import path
from . import views
from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView


urlpatterns = [
    path('', views.UserList.as_view(), name="user_list"),
    path('register/', views.RegisterUser.as_view(), name="register_user"),
    path('user-detail/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('login/',
         LoginView.as_view(redirect_field_name="nextpage"), name="login"),
    path('reset-password/',
         PasswordResetView.as_view(template_name="registration/reset_form.html",
                                   subject_template_name="registration/reset_subject.txt"), name="reset_password"),
    path('reset-password-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name="registration/reset_form_confirm.html"), name="password_reset_confirm"),
    path('reset-password-done/',
         TemplateView.as_view(template_name="registration/reset_form_done.html"), name="password_reset_done"),
    path('reset-password-complete/',
         TemplateView.as_view(template_name="registration/reset_form_complete.html"), name="password_reset_complete"),
]
