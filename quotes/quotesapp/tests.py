from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Quote, Tag

# Тестування функціоналу додатка
class QuoteAppTests(TestCase):
    # Налаштування перед кожним тестом
    def setUp(self):
        # Створення користувача для тестування
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Створення тестового автора
        self.author = Author.objects.create(fullname='Test Author', born_date='2000-01-01', born_location='Test Location', description='Test Description')
        # Створення тестової цитати
        self.quote = Quote.objects.create(author=self.author, quote='Test Quote')

    # Тести для перевірки відображення сторінок
    def test_main_view(self):
        # Перевірка головної сторінки
        response = self.client.get(reverse('quotesapp:main'))
        # Перевірка коду відповіді
        self.assertEqual(response.status_code, 200)
        # Перевірка використаного шаблону
        self.assertTemplateUsed(response, 'quotesapp/index.html')

    def test_create_author_view(self):
        # Перевірка сторінки створення автора
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('quotesapp:create_author'))
        # Перевірка коду відповіді
        self.assertEqual(response.status_code, 200)
        # Перевірка використаного шаблону
        self.assertTemplateUsed(response, 'quotesapp/create_author.html')

    def test_create_quote_view(self):
        # Перевірка сторінки створення цитати
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('quotesapp:create_quote'))
        # Перевірка коду відповіді
        self.assertEqual(response.status_code, 200)
        # Перевірка використаного шаблону
        self.assertTemplateUsed(response, 'quotesapp/create_quote.html')

    # Тести для перевірки методів __str__() моделей
    def test_author_str_method(self):
        # Перевірка методу __str__() моделі Author
        self.assertEqual(str(self.author), 'Test Author')

    def test_quote_str_method(self):
        # Перевірка методу __str__() моделі Quote
        self.assertEqual(str(self.quote), '"Test Quote" - Test Author')

    # Тести для створення, редагування та видалення авторів
    def test_author_create(self):
        # Перевірка можливості створення автора
        author_count = Author.objects.count()
        Author.objects.create(fullname='New Author', born_date='2000-01-01', born_location='New Location', description='New Description')
        self.assertEqual(Author.objects.count(), author_count + 1)

    def test_author_edit(self):
        # Перевірка можливості редагування автора
        author = Author.objects.get(fullname='Test Author')
        author.fullname = 'Updated Author'
        author.save()
        self.assertEqual(Author.objects.get(pk=author.pk).fullname, 'Updated Author')

    def test_author_delete(self):
        # Перевірка можливості видалення автора
        author_count = Author.objects.count()
        author = Author.objects.get(fullname='Test Author')
        author.delete()
        self.assertEqual(Author.objects.count(), author_count - 1)

    # Тести для створення, редагування та видалення цитат
    def test_quote_create(self):
        # Перевірка можливості створення цитати
        quote_count = Quote.objects.count()
        quote = Quote.objects.create(author=self.author, quote='New Quote')
        self.assertEqual(Quote.objects.count(), quote_count + 1)

    def test_quote_edit(self):
        # Перевірка можливості редагування цитати
        quote = Quote.objects.get(quote='Test Quote')
        quote.quote = 'Updated Quote'
        quote.save()
        self.assertEqual(Quote.objects.get(pk=quote.pk).quote, 'Updated Quote')

    def test_quote_delete(self):
        # Перевірка можливості видалення цитати
        quote_count = Quote.objects.count()
        quote = Quote.objects.get(quote='Test Quote')
        quote.delete()
        self.assertEqual(Quote.objects.count(), quote_count - 1)
