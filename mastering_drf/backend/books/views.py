from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import generics, mixins, permissions
from django.shortcuts import get_object_or_404
from api.permissions import isStaffEditOrView
from api.mixins import (
    UserQuerySetMixin,
    IsStaffOrReadOnlyMixin
)
# @api_view(["GET"])
# def get_books_view(request, *args, **kwargs):
#     """
#     DRF API view
#     """
#     instance = Book.objects.all()
#     data = {}
#     if instance:
#         # data = model_to_dict(book, fields={'id', 'title', 'price', 'sale_price'})
#         data = BookSerializer(instance, many=True).data
#     else:
#         data = {"error": "No books found"}
#     return Response(data)


# @api_view(["POST"])
# def create_book_view(request, *args, **kwargs):
#     newBook = BookSerializer(data=request.data)
#     if newBook.is_valid(raise_exception=True):
#         # instance = newBook.save()
#         # print(instance)
#         print(newBook.data)
#         return Response(newBook.data)
#     return Response({"success": "false", "message": "Invalid Data or missing required fields"}, status=400)


class BookListCreateAPIView(
    UserQuerySetMixin,
    IsStaffOrReadOnlyMixin,
    generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # user_field = 'user'

    def perform_create(self, serializer):
        # print(serializer)
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        author = serializer.validated_data.get('author')
        ISBN = serializer.validated_data.get('ISBN')
        price = serializer.validated_data.get('price')
        sale_price = serializer.validated_data.get('sale_price') or None
        if author is None:
            author = title
        serializer.save(user = self.request.user, author = author)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Book.objects.none()
    #     return qs.filter(user = request.user)

list_create_book_view = BookListCreateAPIView.as_view()

class BookDetailAPIView(
    UserQuerySetMixin,
    IsStaffOrReadOnlyMixin,
    generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser ,isStaffEditOrView] 
    # lookup_field pk

book_detail_view = BookDetailAPIView.as_view()

class BookUpdateAPIView(
    UserQuerySetMixin,
    IsStaffOrReadOnlyMixin,
    generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser ,isStaffEditOrView] 
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

book_update_view = BookUpdateAPIView.as_view()

class BookDestroyAPIView(
    UserQuerySetMixin,
    IsStaffOrReadOnlyMixin,
    generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser ,isStaffEditOrView] 
    lookup_field = 'pk'

    def perform_delete(self, instance):
        # instance
        super().perform_delete(instance)

book_delete_view = BookDestroyAPIView.as_view()

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ProductMixinView(
    mixins.ListModelMixin,
    generics.GenericAPIView
    ):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
product_mixin_view = ProductMixinView.as_view()

@api_view(['GET', 'POST'])
def book_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Book, pk=pk)
            data = BookSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Book.objects.all()
        data = BookSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        # create book api
        newBook = BookSerializer(data=request.data)
        if newBook.is_valid(raise_exception=True):
            ISBN = newBook.validated_data.get('ISBN')   
            if ISBN is None:
                ISBN = "1-2-3-4-5"
            newBook.save(ISBN=ISBN)
            # print(newBook.data)
            return Response(newBook.data)
        return Response({"success": "false", "message": "Invalid Data or missing required fields"}, status=400)