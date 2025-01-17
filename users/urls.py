from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, reset_password, ProfileView, UserLoginView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('reset_password/', reset_password, name='reset_password'),
]
