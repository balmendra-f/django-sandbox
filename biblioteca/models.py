from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nacionalidad} - {self.pais}"

    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Comuna(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    departamento = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        direccion = f"{self.calle} {self.numero}"
        if self.departamento:
            direccion += f", Depto. {self.departamento}"
        direccion += f", {self.id_comuna.nombre}"
        return direccion

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=200)
    id_direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Bibliotecas"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.PositiveIntegerField()
    copias = models.PositiveIntegerField(default=1)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} - {self.id_autor.nombre}"

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


class Lector(models.Model):
    rut = models.CharField(
        max_length=12,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{7,8}-[0-9kK]$', message='Formato de RUT inválido')]
    )
    digito_verificador = models.CharField(max_length=1)
    nombre = models.CharField(max_length=200)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"


class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    plazo_devolucion = models.DateTimeField()
    fecha_entrega = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        estado = "Devuelto" if self.fecha_entrega else "Prestado"
        return f"{self.id_libro.titulo} - {self.id_lector.nombre} ({estado})"

    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"
