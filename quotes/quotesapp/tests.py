from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Quote, Tag

class QuoteAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(fullname='Test Author', born_date='2000-01-01', born_location='Test Location', description='Test Description')
        self.quote = Quote.objects.create(author=self.author, quote='Test Quote')

    # Tests for views
    def test_main_view(self):
        response = self.client.get(reverse('quotesapp:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quotesapp/index.html')

    def test_create_author_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('quotesapp:create_author'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quotesapp/create_author.html')

    def test_create_quote_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('quotesapp:create_quote'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quotesapp/create_quote.html')


    def test_author_str_method(self):
        self.assertEqual(str(self.author), 'Test Author')

    def test_quote_str_method(self):
        self.assertEqual(str(self.quote), '"Test Quote" - Test Author')

    def test_author_create(self):
        author_count = Author.objects.count()
        Author.objects.create(fullname='New Author', born_date='2000-01-01', born_location='New Location', description='New Description')
        self.assertEqual(Author.objects.count(), author_count + 1)

    def test_author_edit(self):
        author = Author.objects.get(fullname='Test Author')
        author.fullname = 'Updated Author'
        author.save()
        self.assertEqual(Author.objects.get(pk=author.pk).fullname, 'Updated Author')

    def test_author_delete(self):
        author_count = Author.objects.count()
        author = Author.objects.get(fullname='Test Author')
        author.delete()
        self.assertEqual(Author.objects.count(), author_count - 1)

   
    def test_quote_create(self):
        quote_count = Quote.objects.count()
        quote = Quote.objects.create(author=self.author, quote='New Quote')
        self.assertEqual(Quote.objects.count(), quote_count + 1)

    def test_quote_edit(self):
        quote = Quote.objects.get(quote='Test Quote')
        quote.quote = 'Updated Quote'
        quote.save()
        self.assertEqual(Quote.objects.get(pk=quote.pk).quote, 'Updated Quote')

    def test_quote_delete(self):
        quote_count = Quote.objects.count()
        quote = Quote.objects.get(quote='Test Quote')
        quote.delete()
        self.assertEqual(Quote.objects.count(), quote_count - 1)
