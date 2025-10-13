from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateListProduct.as_view(), name='create_list_product'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProduct.as_view(), name='retrieve_update_destroy_product'),
]