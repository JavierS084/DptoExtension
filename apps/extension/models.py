from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Alumnos(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=40)
    CI=models.IntegerField()
    email=models.EmailField(blank=True , null=True)
    telefono=models.CharField(max_length=12)
    sede_id=models.ForeignKey('Sedes', null=True, blank=True, on_delete=models.CASCADE,  verbose_name="Sedes")
    carrera_id=models.ForeignKey('Carreras', null=True, blank=True, on_delete=models.CASCADE,  verbose_name="Carrera")
    horaExtension=models.IntegerField( verbose_name="Hora de extension")
    estado=models.BooleanField('Alumno Activo/No Activo', default=True)
    tituloDocumento=models.CharField(max_length=100 ,null=False, blank=True)
    Documento=models.FileField(upload_to="archivos/", null=True, blank=True)

    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    
    class Meta:
        verbose_name='Alumno'
        verbose_name_plural='Alumnos'
        ordering=['apellido']

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    CI=models.IntegerField()
    materia=models.CharField(max_length=50)

    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'

    def __str__(self):
        return self.nombre 

class Carreras(models.Model):
    carrera=models.CharField(max_length=40)

    class Meta:
        verbose_name='Carrera'
        verbose_name_plural='Carreras'

    def __str__(self):
        return self.carrera

class Sedes(models.Model):
    sede=models.CharField(max_length=50)
    
    class Meta:
        verbose_name='Sede'
        verbose_name_plural='Sedes'

    def __str__(self):
        return self.sede

class Proyecto(models.Model):
    tituloProyecto=models.CharField(max_length=100 ,null=False, blank=True)
    descripcion=models.TextField(null=True, blank=True)


    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'

    def __str__(self):
        return self.descripcion    

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria ', max_length=100, null=False, blank=False)
    estado =  models.BooleanField('Categoria Activida/Categoria Desactivada', default=True)
    fecha_creacion =  models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField('Titulo', max_length=90, blank=False, null= False)
    slug=models.CharField('Slug', max_length=100, blank=False, null=False)
    descripcion=models.CharField('Descripcion', max_length=110, blank=False, null=False)
    contenido=RichTextField()
    imagen=RichTextField('imagen',null=True)
    docente=models.ForeignKey('Docente',null=True, blank=True, on_delete=models.CASCADE)
    categoria=models.ForeignKey('Categoria', blank=False, null= False, on_delete=models.CASCADE)
    estado=models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion=models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo