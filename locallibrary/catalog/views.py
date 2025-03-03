from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre
from django.db.models import Q


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Count total genres
    num_genres = Genre.objects.count()

    # Count books containing a specific word (e.g., "adventure", case insensitive)
    search_word = "harry"
    num_books_with_word = Book.objects.filter(title__icontains=search_word).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_word': num_books_with_word,
        'search_word': search_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

