from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # localhost:8000/api/
    path('api/books/', include('books.urls')),
    path('api/v2/', include('drf1.routers')),
    path('api/product/', include('product.urls')),
    # path('api/search', include('search.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
  