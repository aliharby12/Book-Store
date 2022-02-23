from django.views.generic import ListView, DetailView

from project.store.models import Book


class BookListView(ListView):
    """view to list all books"""
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    ordering = ['-created']


class BookDetailView(DetailView):
    """view to show a book details"""
    model = Book
    context_name = 'book'
    template_name = 'detail.html'