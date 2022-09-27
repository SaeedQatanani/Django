from django.shortcuts import render, redirect
from .models import Book, Author

def index_books(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)

def add_book(request):
    Book.objects.create(title = request.POST['title'],
                        desc = request.POST['desc'])
    return redirect('/')

def show_book(request, book_id):
    book = Book.objects.get(id = book_id)
    context = {
        'book': book,
        'this_book_authors': book.authors.all(),
        'authors' : Author.objects.all(),
    }
    return render(request, 'show.html', context)

def add_author_to_book(request, book_id):
    author_id = int(request.POST['authors'])
    book = Book.objects.get(id = book_id)
    book.authors.add(Author.objects.get(id = author_id))
    return redirect('/books/'+str(book_id))


def index_authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'authors_index.html', context)

def add_author(request):
    Author.objects.create(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        notes = request.POST['notes']
                        )
    return redirect('/authors')

def show_author(request, author_id):
    author = Author.objects.get(id = author_id)
    context = {
        'author': author,
        'this_author_books': author.books.all(),
        'books' : Book.objects.all(),
    }
    return render(request, 'authors_show.html', context)

def add_book_to_author(request, author_id):
    book_id = int(request.POST['books'])
    author = Author.objects.get(id = author_id)
    author.books.add(Book.objects.get(id = book_id))
    return redirect('/authors/'+str(author_id))
