from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.product_list),
    path("orders/", views.order_list),
    path("info/<int:pk>/", views.product_detail),
]