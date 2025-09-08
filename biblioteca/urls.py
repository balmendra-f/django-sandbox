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
router.register(r'nacionalidades', NacionalidadViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'comunas', ComunaViewSet)
router.register(r'direcciones', DireccionViewSet)
router.register(r'bibliotecas', BibliotecaViewSet)
router.register(r'libros', LibroViewSet)
router.register(r'lectores', LectorViewSet)
router.register(r'prestamos', PrestamoViewSet)

# ⚠️ IMPORTANTE: urlpatterns debe ser una lista
urlpatterns = [
    path('', include(router.urls)),
]
