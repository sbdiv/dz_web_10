from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm, TagForm
from .models import Quote, Author
from django.contrib.auth.decorators import login_required

# Вигляд для головної сторінки
def main(request):
    """
    Відображає головну сторінку додатка.
    """
    return render(request, 'quotesapp/index.html')

# Вигляд для створення нового автора
@login_required
def create_author(request):
    """
    Відображає форму для створення нового автора. Після надсилання форми зберігає дані нового автора у випадку успішності.
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')  
    else:
        form = AuthorForm()
    return render(request, 'quotesapp/create_author.html', {'form': form})

# Вигляд для створення нової цитати
@login_required
def create_quote(request):
    """
    Відображає форму для створення нової цитати. Після надсилання форми зберігає дані нової цитати у випадку успішності.
    """
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')  
    else:
        form = QuoteForm()
    return render(request, 'quotesapp/create_quote.html', {'form': form})

# Вигляд для створення нового тегу
@login_required
def tag(request):
    """
    Відображає форму для створення нового тегу. Після надсилання форми зберігає дані нового тегу у випадку успішності.
    """
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')  
    else:
        form = TagForm()
    return render(request, 'quotesapp/tag.html', {'form': form})

# Вигляд для відображення всіх цитат
def quotes_view(request):
    """
    Відображає всі цитати, які зберігаються у базі даних.
    """
    quotes = Quote.objects.all()
    return render(request, 'quotesapp/quotes.html', {'quotes': quotes})

# Вигляд для відображення всіх авторів
def authors(request):
    """
    Відображає всіх авторів, які зберігаються у базі даних.
    """
    authors = Author.objects.all()
    return render(request, 'quotesapp/authors.html', {'authors': authors})

# Вигляд для детального перегляду автора
def author_detail(request, author_id):
    """
    Відображає деталі про конкретного автора на основі його ідентифікатора.
    """
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'quotesapp/author_detail.html', {'author': author})
