from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from common.view import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()


class UserLoginForm(StyleFormMixin, AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password')
