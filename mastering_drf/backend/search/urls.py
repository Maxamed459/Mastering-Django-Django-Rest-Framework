from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookSearchList.as_view(), name="search")
]