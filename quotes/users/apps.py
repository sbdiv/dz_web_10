from django.apps import AppConfig

# Клас конфігурації для додатка Django з ім'ям "Users"
class UsersConfig(AppConfig):
    # Використовується велике автоматичне поле для ID моделей за замовчуванням
    default_auto_field = 'django.db.models.BigAutoField'
    # Ім'я додатка
    name = 'users'
