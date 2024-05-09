from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Форма реєстрації користувача
class RegisterForm(UserCreationForm):
    # Поля для ім'я користувача та пароль
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Форма входу користувача
class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

# Форма скидання пароля        
class ResetPasswordForm(forms.Form):
    # Поле для введення ім'я користувача або електронної пошти
    username = forms.CharField(max_length=100, required=True, label='Username or Email')