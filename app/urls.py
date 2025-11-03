from django.contrib import admin
from django.urls import include, path
from app import views  # importamos nuestras vistas

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentacion API Biblioteca",
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
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),  # URLs de la app biblioteca
    path('', views.home_template, name='home'),  # home page
    path('libros/', views.listado_libros, name='listado_libros'),  # listado de libros
    
    # Documentación drf-yasg
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]