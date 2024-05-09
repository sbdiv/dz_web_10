from django.contrib import admin
from .models import Author, Quote, Tag

# Реєстрація моделі Author у панелі адміністратора
admin.site.register(Author)

# Реєстрація моделі Quote у панелі адміністратора
admin.site.register(Quote)

# Реєстрація моделі Tag у панелі адміністратора
admin.site.register(Tag)
