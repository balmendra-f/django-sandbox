# /app/urls.py
from django.contrib import admin
from django.urls import path, include
from app import views  # nuestras vistas
from django.contrib.auth import views as auth_views

# DRF + drf-yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación API Biblioteca",
        default_version='v1',
        description="Mi_Aplication",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mi_correo@test.test"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App biblioteca
    path('api/', include('biblioteca.urls')),  # URLs de la app biblioteca

    # Home
    path('', views.home_template, name='home'),

    # Listado de libros (login requerido)
    path('libros/', views.listado_libros, name='listado_libros'),

    # Autenticación
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/registro/', views.registro, name='registro'),

    # Documentación DRF (Swagger / Redoc)
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
