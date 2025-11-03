from django.contrib import admin
from .models import (
    Nacionalidad,
    Autor,
    Comuna,
    Direccion,
    Biblioteca,
    Libro,
    Lector,
    Prestamo
)


@admin.register(Nacionalidad)
class NacionalidadAdmin(admin.ModelAdmin):
    list_display = ('nacionalidad', 'pais')
    search_fields = ('nacionalidad', 'pais')
    list_filter = ('pais',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id_nacionalidad', 'bio_preview')
    search_fields = ('nombre', 'bio', 'pseudonimo')
    list_filter = ('id_nacionalidad',)
    raw_id_fields = ('id_nacionalidad',)

    def bio_preview(self, obj):
        if obj.bio:
            return obj.bio[:50] + "..." if len(obj.bio) > 50 else obj.bio
        return "-"
    bio_preview.short_description = 'Biografía'


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')
    ordering = ('codigo',)


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'departamento', 'id_comuna')
    search_fields = ('calle', 'numero', 'id_comuna__nombre')
    list_filter = ('id_comuna',)
    raw_id_fields = ('id_comuna',)


@admin.register(Biblioteca)
class BibliotecaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_direccion')
    search_fields = ('nombre', 'id_direccion__calle')
    raw_id_fields = ('id_direccion',)

    def get_direccion(self, obj):
        return str(obj.id_direccion)
    get_direccion.short_description = 'Dirección'


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id_autor', 'paginas', 'copias', 'id_biblioteca', 'habilitado')
    search_fields = ('titulo', 'id_autor__nombre')
    list_filter = ('id_biblioteca', 'habilitado', 'id_autor')
    raw_id_fields = ('id_autor', 'id_biblioteca')
    list_editable = ('copias', 'habilitado')


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'get_direccion', 'id_biblioteca', 'habilitado')
    search_fields = ('nombre', 'rut')
    list_filter = ('id_biblioteca', 'habilitado')
    raw_id_fields = ('id_direccion', 'id_biblioteca')
    list_editable = ('habilitado',)

    def get_direccion(self, obj):
        return f"{obj.id_direccion.calle} {obj.id_direccion.numero}"
    get_direccion.short_description = 'Dirección'


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id_libro', 'id_lector', 'fecha_prestamo', 'plazo_devolucion', 'fecha_entrega', 'estado')
    search_fields = ('id_libro__titulo', 'id_lector__nombre', 'id_lector__rut')
    list_filter = ('fecha_prestamo', 'plazo_devolucion', 'fecha_entrega')
    raw_id_fields = ('id_libro', 'id_lector')
    date_hierarchy = 'fecha_prestamo'

    def estado(self, obj):
        return "Devuelto" if obj.fecha_entrega else "Prestado"
    estado.short_description = 'Estado'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('fecha_prestamo',)
        return self.readonly_fields
