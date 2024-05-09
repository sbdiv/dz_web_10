from django.urls import path
from . import views

app_name = 'users'  # Простір імен додатка

urlpatterns = [
    # URL для реєстрації нового користувача
    path('signup/', views.signupuser, name='signup'),

    # URL для входу користувача
    path('login/', views.loginuser, name='login'),

    # URL для виходу користувача
    path('logout/', views.logoutuser, name='logout'),

    # URL для запиту на скидання пароля
    path('reset-password/', views.reset_password_request, name='reset-password'),

    # URL для підтвердження скидання пароля за допомогою токена
    path('reset-password/<str:token>/', views.reset_password_request, name='reset-password-confirm'),
]
