from django.urls import path

from project.store.views import BookListView, BookDetailView

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail')
]
