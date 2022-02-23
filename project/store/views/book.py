from django.views.generic import ListView, DetailView
from django.db.models import Q

from project.store.models import Book


class BookListView(ListView):
    """view to list all books"""
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    ordering = ['-created']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            books = self.model.objects.filter(Q(title__icontains=query) | Q(price__iexact=query), Q(amount__gte=1))
        else:
            books = self.model.objects.filter(amount__gte=1)
        return books


class BookDetailView(DetailView):
    """view to show a book details"""
    model = Book
    context_name = 'book'
    template_name = 'detail.html'