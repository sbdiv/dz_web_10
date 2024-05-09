from django.apps import AppConfig

# Визначаємо спеціальну конфігурацію для додатка 'quotesapp'
class QuotesappConfig(AppConfig):
    # Встановлюємо тип авто-поля за замовчуванням для моделей у цьому додатку
    default_auto_field = 'django.db.models.BigAutoField'
    # Вказуємо назву додатка
    name = 'quotesapp'
