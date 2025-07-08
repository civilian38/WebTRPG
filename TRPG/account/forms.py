from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import TRPGUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = TRPGUser
        fields = ('username', 'nickname', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass  # 기본 필드로 충분함