from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Biblioteca API",
        default_version="v1",
        description="Documentación interactiva de la API de la Biblioteca",
        contact=openapi.Contact(email="soporte@biblioteca.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),
    path('', views.home_template, name='home'),
    path('libros/', views.listado_libros, name='listado_libros'),
    path('nacionalidades/', views.listado_nacionalidades, name='listado_nacionalidades'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
