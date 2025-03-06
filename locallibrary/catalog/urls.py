from django.urls import path
from . import views

urlpatterns = [
    # catalog/ — The home (index) page.
    path("", views.index, name="index"),

    # catalog/books/ — A list of all books.
    path("books/", views.BookListView.as_view(), name="books"),

    # catalog/authors/ — A list of all authors.
    path("authors/", views.AuthorListView.as_view(), name="authors"),

    # catalog/book/<id> — The detail view for a particular book, with a field primary key of <id> (the default). 
    # For example, the URL for the third book added to the list will be /catalog/book/3.
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),

    # catalog/author/<id> — The detail view for the specific author with a primary key field of <id>. 
    # For example, the URL for the 11th author added to the list will be /catalog/author/11.
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),

    # part 8: for viewing the books a user has borrowed
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    # part 8 challenge: for viewing all borrowed books
    path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),

    # part 9: URL configuration for the renew-books page
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    # part 9: URL configuration for the author create, update, and delete pages
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
