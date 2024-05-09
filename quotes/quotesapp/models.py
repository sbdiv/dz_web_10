from django.db import models

# Модель для представлення авторів
class Author(models.Model):
    fullname = models.CharField(max_length=100)  # Повне ім'я автора
    born_date = models.CharField(max_length=20)  # Дата народження автора
    born_location = models.CharField(max_length=100)  # Місце народження автора
    description = models.TextField()  # Опис автора

    def __str__(self):
        return self.fullname  # Повертаємо повне ім'я автора як рядок

# Модель для представлення цитат
class Quote(models.Model):
    tags = models.ManyToManyField('Tag', related_name='quotes')  # Теги, пов'язані з цитатою
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Автор цитати
    quote = models.TextField()  # Текст цитати

    def __str__(self):
        return f'"{self.quote}" - {self.author.fullname}'  # Повертаємо рядок, що містить текст цитати та повне ім'я автора

# Модель для представлення тегів
class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)  # Назва тегу

    def __str__(self):
        return self.name  # Повертаємо назву тегу як рядок
