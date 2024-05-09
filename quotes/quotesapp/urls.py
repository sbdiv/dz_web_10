from django.urls import path
from . import views

# Простір імен для додатка
app_name = 'quotesapp'

# Список URL шляхів
urlpatterns = [
    # Головна сторінка, відображається список цитат
    path('', views.main, name='main'),
    # Шлях для створення нової цитати
    path('quote/', views.create_quote, name='create_quote'),
    # Шлях для перегляду тегів
    path('tag/', views.tag, name='tag'),
    # Шлях для перегляду всіх цитат
    path('quotes/', views.quotes_view, name='quotes'),
    # Шлях для перегляду всіх авторів
    path('authors/', views.authors, name='authors'),
    # Шлях для створення нового автора
    path('author/create/', views.create_author, name='create_author'),
    # Шлях для детального перегляду автора за його ідентифікатором
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]
