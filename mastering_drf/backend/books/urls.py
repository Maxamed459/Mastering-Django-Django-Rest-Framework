from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_create_book_view), # listing books using generics.GenericAPIView mixins.ListModelMixin
    path('<int:pk>/update', views.book_update_view),
    path('<int:pk>/delete', views.book_delete_view),
    path('<int:pk>/', views.book_detail_view),
    # path('', views.book_alt_view, name='book-list'),           # GET all books / POST new
    # path('<int:pk>/', views.book_alt_view, name='book-detail') # GET single book
]