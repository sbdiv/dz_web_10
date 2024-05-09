from django import forms
from .models import Author, Quote, Tag

# Форма для моделі Author
class AuthorForm(forms.ModelForm):
    class Meta:
        # Вказуємо, що ця форма базується на моделі Author
        model = Author
        # Поля, які будуть відображені у формі, включають повне ім'я, дату народження,
        # місце народження та опис автора
        fields = ['fullname', 'born_date', 'born_location', 'description']

# Форма для моделі Quote
class QuoteForm(forms.ModelForm):
    class Meta:
        # Вказуємо, що ця форма базується на моделі Quote
        model = Quote
        # Поля, які будуть відображені у формі, включають теги, автора та сам цитату
        fields = ['tags', 'author', 'quote']

# Форма для моделі Tag
class TagForm(forms.ModelForm):
    class Meta:
        # Вказуємо, що ця форма базується на моделі Tag
        model = Tag
        # Поле, яке буде відображене у формі, є лише назва тегу
        fields = ['name']
