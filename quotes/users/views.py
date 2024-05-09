from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ResetPasswordForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.conf import settings

# Функція для обробки запиту на скидання пароля
def reset_password_request(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            # Отримання інформації з форми
            username_or_email = form.cleaned_data.get('username')

            try:
                # Спроба знайти користувача за ім'ям користувача
                user = User.objects.get(username=username_or_email)
            except User.DoesNotExist:
                try:
                    # Спроба знайти користувача за електронною адресою
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    # Якщо користувача не знайдено, вивести повідомлення про помилку
                    form.add_error('username', 'User with this username or email does not exist.')
                    return render(request, 'your_app/reset_password.html', {'form': form})

            # Генерування токену та створення URL для скидання пароля
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_password_url = f"{settings.BASE_URL}/reset-password/{uid}/{token}/"

            # Підготовка та відправка листа для скидання пароля
            subject = 'Reset your password'
            message = render_to_string('your_app/reset_password_email.html', {'reset_password_url': reset_password_url})
            sender_email = settings.DEFAULT_FROM_EMAIL
            recipient_email = user.email
            send_mail(subject, message, sender_email, [recipient_email])

            # Відображення сторінки успішного скидання пароля
            return render(request, 'your_app/reset_password_success.html')
    else:
        # Відображення форми скидання пароля для GET-запиту
        form = ResetPasswordForm()
    return render(request, 'your_app/reset_password.html', {'form': form})


# Функція для реєстрації нового користувача
def signupuser(request):
    if request.user.is_authenticated:
        # Перенаправлення користувача на головну сторінку, якщо він вже аутентифікований
        return redirect(to='quotesapp:main')

    if request.method == 'POST':
        # Обробка POST-запиту на реєстрацію
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Збереження нового користувача та перенаправлення на головну сторінку
            form.save()
            return redirect(to='quotesapp:main')
        else:
            # Повернення форми реєстрації з повідомленнями про помилки, якщо форма недійсна
            return render(request, 'users/signup.html', context={"form": form})

    # Відображення форми реєстрації для GET-запиту
    return render(request, 'users/signup.html', context={"form": RegisterForm()})


# Функція для входу користувача
def loginuser(request):
    if request.user.is_authenticated:
        # Перенаправлення користувача на головну сторінку, якщо він вже аутентифікований
       return redirect(to='quotesapp:main')

    if request.method == 'POST':
        # Обробка POST-запиту на вхід користувача
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Виведення повідомлення про помилку, якщо аутентифікація не вдалася
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        # Успішний вхід користувача та перенаправлення на головну сторінку
        login(request, user)
        return redirect(to='quotesapp:main')

    # Відображення форми входу для GET-запиту
    return render(request, 'users/login.html', context={"form": LoginForm()})


# Функція для виходу користувача
@login_required
def logoutuser(request):
    # Вихід користувача та перенаправлення на головну сторінку
    logout(request)
    return redirect(to='quotesapp:main')
