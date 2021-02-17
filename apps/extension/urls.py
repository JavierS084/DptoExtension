from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns=[
    path('perfil/',login_required(Perfil.as_view()), name='perfil'),
    path('crearalumno/',CrearAlumno.as_view(), name='crearAlumno'),
    path('certificados/',login_required(EntregaCertificado.as_view()), name='certificado'),
    path('convenios/',Convenio.as_view(), name='convenio'),
    path('bienestar/', Bienestar.as_view(), name='bienestar'),
    path('docentesinvestigadores/', DocentesI.as_view(), name='investigadores'),
    path('certificacion/', Certificacion_online.as_view(), name='certificacion'),
    path('politica/', Politica_investigacion.as_view(), name='politica'),
    path('formato/', Formato.as_view(), name='formato'),
    path('trabajofinales/', Trabajos_Finales.as_view(), name='trabajofinales'),
    path('guiatrabajo/', GuiaTrabajoFinal.as_view(), name='guiatrabajofinales'),
    path('manualcitas/', ManualBiblograficas.as_view(), name='manualbiblograficas'),
    path('normas/', NormaIso.as_view(), name='normaiso'),
    path('reglamento/', ReglamentoTFG.as_view(), name='reglamento'),
    path('blog/',Blog.as_view(), name='blog'),
    path('about/', about, name='about'),
    path('courses/',Courses.as_view(), name='courses'),
    path('listalumno/',login_required(ListadoAlumno.as_view()), name='lista_alumno'), 
    path('editalumno/<int:pk>',ActualizarAlumnos.as_view(), name='edit_alumno'),
    path('deletealumno/<int:pk>',EliminarAlumno.as_view(), name='delete_alumno' ),
  
    
]