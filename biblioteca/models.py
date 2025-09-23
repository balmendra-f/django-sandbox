from django.db import models
from django.core.validators import RegexValidator


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    
    def registrar_nacionalidad(self):
        self.save()
        return f"Nacionalidad {self.nacionalidad} registrada exitosamente"
    
    def obtener_nacionalidad(self):
        return self
    
    def actualizar_nacionalidad(self, pais=None, nacionalidad=None):
        if pais:
            self.pais = pais
        if nacionalidad:
            self.nacionalidad = nacionalidad
        self.save()
        return f"Nacionalidad actualizada exitosamente"
    
    def eliminar_nacionalidad(self):
        nacionalidad_nombre = self.nacionalidad
        self.delete()
        return f"Nacionalidad {nacionalidad_nombre} eliminada exitosamente"
    
    def __str__(self):
        return f"{self.nacionalidad} - {self.pais}"
    
    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    
    def registrar_autor(self):
        self.save()
        return f"Autor {self.nombre} registrado exitosamente"
    
    def obtener_autor(self):
        return self
    
    def actualizar_autor(self, nombre=None, bio=None, id_nacionalidad=None):
        if nombre:
            self.nombre = nombre
        if bio:
            self.bio = bio
        if id_nacionalidad:
            self.id_nacionalidad = id_nacionalidad
        self.save()
        return f"Autor {self.nombre} actualizado exitosamente"
    
    def eliminar_autor(self):
        nombre_autor = self.nombre
        self.delete()
        return f"Autor {nombre_autor} eliminado exitosamente"
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Comuna(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=100)
    
    def registrar_comuna(self):
        self.save()
        return f"Comuna {self.nombre} registrada exitosamente"
    
    def obtener_comuna(self):
        return self
    
    def actualizar_comuna(self, codigo=None, nombre=None):
        if codigo:
            self.codigo = codigo
        if nombre:
            self.nombre = nombre
        self.save()
        return f"Comuna {self.nombre} actualizada exitosamente"
    
    def eliminar_comuna(self):
        nombre_comuna = self.nombre
        self.delete()
        return f"Comuna {nombre_comuna} eliminada exitosamente"
    
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
    
    def registrar_direccion(self):
        self.save()
        return f"Dirección registrada exitosamente"
    
    def obtener_direccion(self):
        return self
    
    def actualizar_direccion(self, calle=None, numero=None, departamento=None, id_comuna=None):
        if calle:
            self.calle = calle
        if numero:
            self.numero = numero
        if departamento is not None:
            self.departamento = departamento
        if id_comuna:
            self.id_comuna = id_comuna
        self.save()
        return f"Dirección actualizada exitosamente"
    
    def eliminar_direccion(self):
        self.delete()
        return f"Dirección eliminada exitosamente"
    
    def __str__(self):
        direccion_completa = f"{self.calle} {self.numero}"
        if self.departamento:
            direccion_completa += f", Depto. {self.departamento}"
        direccion_completa += f", {self.id_comuna.nombre}"
        return direccion_completa
    
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=200)
    id_direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    
    def registrar_biblioteca(self):
        self.save()
        return f"Biblioteca {self.nombre} registrada exitosamente"
    
    def obtener_biblioteca(self):
        return self
    
    def actualizar_biblioteca(self, nombre=None, id_direccion=None):
        if nombre:
            self.nombre = nombre
        if id_direccion:
            self.id_direccion = id_direccion
        self.save()
        return f"Biblioteca {self.nombre} actualizada exitosamente"
    
    def eliminar_biblioteca(self):
        nombre_biblioteca = self.nombre
        self.delete()
        return f"Biblioteca {nombre_biblioteca} eliminada exitosamente"
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Biblioteca"
        verbose_name_plural = "Bibliotecas"


class Libro(models.Model):
    titulo = models.CharField(max_length=300)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    paginas = models.PositiveIntegerField()
    copias = models.PositiveIntegerField(default=1)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)
    
    def registrar_libro(self):
        self.save()
        return f"Libro '{self.titulo}' registrado exitosamente"
    
    def buscar_libro(self):
        return self
    
    def actualizar_libro(self, titulo=None, paginas=None, copias=None, habilitado=None):
        if titulo:
            self.titulo = titulo
        if paginas:
            self.paginas = paginas
        if copias is not None:
            self.copias = copias
        if habilitado is not None:
            self.habilitado = habilitado
        self.save()
        return f"Libro '{self.titulo}' actualizado exitosamente"
    
    def eliminar_libro(self):
        """Elimina el libro del sistema"""
        titulo_libro = self.titulo
        self.delete()
        return f"Libro '{titulo_libro}' eliminado exitosamente"
    
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
    
    def agregar_lector(self):
        self.save()
        return f"Lector {self.nombre} agregado exitosamente"
    
    def buscar_lector(self):
        return self
    
    def actualizar_lector(self, nombre=None, id_direccion=None, habilitado=None):
        if nombre:
            self.nombre = nombre
        if id_direccion:
            self.id_direccion = id_direccion
        if habilitado is not None:
            self.habilitado = habilitado
        self.save()
        return f"Lector {self.nombre} actualizado exitosamente"
    
    def eliminar_lector(self):
        nombre_lector = self.nombre
        self.delete()
        return f"Lector {nombre_lector} eliminado exitosamente"
    
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
    
    def prestar_libro(self):
        if self.id_libro.copias > 0 and self.id_lector.habilitado:
            self.id_libro.copias -= 1
            self.id_libro.save()
            self.save()
            return f"Préstamo registrado: '{self.id_libro.titulo}' a {self.id_lector.nombre}"
        else:
            return "No se puede realizar el préstamo: libro sin copias disponibles o lector inhabilitado"
    
    def devolver_libro(self):
        if not self.fecha_entrega:
            self.fecha_entrega = models.timezone.now()
            self.id_libro.copias += 1
            self.id_libro.save()
            self.save()
            return f"Libro '{self.id_libro.titulo}' devuelto por {self.id_lector.nombre}"
        else:
            return "Este libro ya fue devuelto"
    
    def aplazar_entrega(self, nuevo_plazo):
        if not self.fecha_entrega:
            self.plazo_devolucion = nuevo_plazo
            self.save()
            return f"Plazo de devolución aplazado hasta {nuevo_plazo}"
        else:
            return "No se puede aplazar: el libro ya fue devuelto"
    
    def __str__(self):
        estado = "Devuelto" if self.fecha_entrega else "Prestado"
        return f"{self.id_libro.titulo} - {self.id_lector.nombre} ({estado})"
    
    class Meta:
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"