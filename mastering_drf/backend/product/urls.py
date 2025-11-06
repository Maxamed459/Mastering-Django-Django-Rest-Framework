from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.ListProductAPIView.as_view()),
    path("orders/", views.OrderListAPIView.as_view()),
    path("user-orders/", views.UserOrderListAPIView.as_view(), name="user-orders"),
    path("info/<int:pk>/", views.RetrieveProductAPIView.as_view()),
]