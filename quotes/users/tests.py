from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm

class UserTests(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'password123',
        }

        self.test_user = User.objects.create_user(**self.user_data)

    def test_register_view(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')



    def test_register_user_invalid_data(self):
        invalid_data = {'username': '', 'password1': 'password123', 'password2': 'password123'}
        response = self.client.post(reverse('users:signup'), invalid_data)
        self.assertEqual(response.status_code, 200)  

    def test_login_view(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_valid_data(self):
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'password123'})
        self.assertRedirects(response, reverse('quotesapp:main'))  
    def test_login_invalid_data(self):
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)  

    def test_logout_user(self):
        self.client.login(username='testuser', password='password123')  
        response = self.client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('quotesapp:main'))  