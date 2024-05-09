from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

# Клас тестів для перевірки функціоналу користувачів
class UserTests(TestCase):
    def setUp(self):
        # Підготовка тестових даних користувача
        self.user_data = {
            'username': 'testuser',
            'password': 'password123',
        }
        # Створення тестового користувача
        self.test_user = User.objects.create_user(**self.user_data)

    # Тест для перевірки відображення сторінки реєстрації користувача
    def test_register_view(self):
        """
        Перевіряє, чи правильно відображається сторінка реєстрації користувача.
        """
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    # Тест для перевірки введення недійсних даних під час реєстрації користувача
    def test_register_user_invalid_data(self):
        """
        Перевіряє, чи залишає користувача на сторінці реєстрації при надсиланні недійсних даних.
        """
        invalid_data = {'username': '', 'password1': 'password123', 'password2': 'password123'}
        response = self.client.post(reverse('users:signup'), invalid_data)
        self.assertEqual(response.status_code, 200)  

    # Тест для перевірки відображення сторінки входу користувача
    def test_login_view(self):
        """
        Перевіряє, чи правильно відображається сторінка входу користувача.
        """
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    # Тест для успішного входу користувача з правильними даними
    def test_login_valid_data(self):
        """
        Перевіряє, чи відбувається успішний вхід користувача з правильними даними.
        """
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'password123'})
        self.assertRedirects(response, reverse('quotesapp:main'))  

    # Тест для входу користувача з неправильними даними
    def test_login_invalid_data(self):
        """
        Перевіряє, чи залишає користувача на сторінці входу при надсиланні неправильних даних.
        """
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)  

    # Тест для виходу користувача
    def test_logout_user(self):
        """
        Перевіряє, чи відбувається успішний вихід користувача.
        """
        self.client.login(username='testuser', password='password123')  
        response = self.client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('quotesapp:main'))  
