from django.shortcuts import render
from rest_framework import generics, filters
from books.models import Book
from books.serializers import BookSerializer

# Create your views here.

class BookSearchList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # using default DRF SearchFilter it uses ?search=rich
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

    # this is the custom one it uses ?q=rich
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        results = Book.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user)
        return results