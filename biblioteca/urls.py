from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from core.views import APIRootView, CustomAuthToken, UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_urls'),
    path('api/', include('core.urls'), name='core_urls'),
    path('api/token/', CustomAuthToken.as_view(), name='api-token'),
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    
    # Endpoints para a documentação da API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]