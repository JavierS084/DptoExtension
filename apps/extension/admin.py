from django.contrib import admin
from import_export import resources 
from import_export.admin import ImportExportModelAdmin
from .models import Alumnos, Carreras, Sedes, Docente, Proyecto, Categoria, Post
# Register your models here.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria
class AlumnosResource(resources.ModelResource):
    class Meta:
        model=Alumnos



class AlumnosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("nombre", "apellido", "CI", "sede_id","carrera_id", "horaExtension", "estado", "user")
    search_fields=("nombre","apellido","CI")
    list_filter=("sede_id",)
    resource_class=AlumnosResource
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','user')
        }),
    )

class DocenteAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "CI", "materia")

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=["nombre"]
    list_display=("nombre", "estado", "fecha_creacion")
    resource_class = CategoriaResource



admin.site.register(Alumnos, AlumnosAdmin)
admin.site.register(Carreras)
admin.site.register(Sedes)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Proyecto)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post)
