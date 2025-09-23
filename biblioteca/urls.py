from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NacionalidadViewSet,
    AutorViewSet,
    ComunaViewSet,
    DireccionViewSet,
    BibliotecaViewSet,
    LibroViewSet,
    LectorViewSet,
    PrestamoViewSet
)

router = DefaultRouter()
router.register(r'nacionalidades', NacionalidadViewSet, basename='nacionalidad')
router.register(r'autores', AutorViewSet, basename='autor')
router.register(r'comunas', ComunaViewSet, basename='comuna')
router.register(r'direcciones', DireccionViewSet, basename='direccion')
router.register(r'bibliotecas', BibliotecaViewSet, basename='biblioteca')
router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'lectores', LectorViewSet, basename='lector')
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')

urlpatterns = [
    path('', include(router.urls)),
]
