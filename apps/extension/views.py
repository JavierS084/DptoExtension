from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, FormView
from django.urls import reverse_lazy
from .forms import Alumnosform
from .models import Alumnos, Categoria, Post

# Create your views here.


class Inicio(TemplateView):
    template_name='inicio/index.html'
    def get(self, request, *args, **kwargs):
        post= Post.objects.filter(estado=True, 
        categoria=Categoria.objects.get(nombre__iexact='general'))

        act=Post.objects.filter(estado=True, 
        categoria=Categoria.objects.get(nombre__iexact='general_actividades'))
        paginator=Paginator(act, 3)
        page=request.GET.get('page')
        act=paginator.get_page(page)
        return render(request,self.template_name ,{'post':post, 'act':act})
        

class Courses (TemplateView):
    template_name='inicio/courses.html'
    def get(self, request, *args, **kwargs):

        actP = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact='actividadPrincipal'))
        act=Post.objects.filter(estado=True, 
        categoria=Categoria.objects.get(nombre__iexact='actividadSecundario'))
        
        return render(request, self.template_name, { 'act':act, 'actP':actP})

class Blog (TemplateView):
    template_name='inicio/blog.html'
    def get(self, request, *args, **kwargs):
        noticia = Post.objects.filter(estado=True,
        categoria=Categoria.objects.get(nombre__iexact='noticiaPrincipal'))
        return render(request, self.template_name, {'noticia':noticia})

class Perfil(TemplateView):
    template_name='extension/perfil.html'


class Convenio(TemplateView):
    template_name='extension/convenios.html'


class Bienestar(TemplateView):
    template_name='extension/bienestar.html'

class DocentesI(TemplateView):
    template_name='investigacion/docenteinvestigadores.html'


class Certificacion_online(TemplateView):
    template_name='investigacion/certificaciononline.html'

class Formato(TemplateView):
    template_name='investigacion/formato.html'
  

class Politica_investigacion(TemplateView):
    template_name='investigacion/politicainvestigacion.html'
  
class Trabajos_Finales(TemplateView):
    template_name='investigacion/trabajofinales.html'

class GuiaTrabajoFinal(TemplateView):
    template_name='investigacion/guiatrabajofinal.html'

class ManualBiblograficas(TemplateView):
    template_name='investigacion/manualbiblograficas.html'

class NormaIso(TemplateView):
    template_name='investigacion/normaiso.html'

class ReglamentoTFG(TemplateView):
    template_name='investigacion/reglamentotfg.html'

class ListadoAlumno(ListView):
    model = Alumnos
    template_name='extension/lista_alumno.html'
    context_object_name='alumnolist'
    queryset=Alumnos.objects.filter(estado=True) 
   # def get(self,request,*args,**kwargs):

class EntregaCertificado(CreateView):
    model=Alumnos
    form_class=Alumnosform
    template_name='extension/entrega_certificados.html'
    success_url = reverse_lazy('extension:perfil')


class ActualizarAlumnos(UpdateView):
    model=Alumnos
    template_name='extension/crear_alumno.html'
    form_class=Alumnosform
    success_url = reverse_lazy('extension:lista_alumno')

class CrearAlumno(CreateView):
    model=Alumnos
    form_class=Alumnosform
    template_name='extension/crear_alumno.html'
    success_url = reverse_lazy('extension:lista_alumno')

class EliminarAlumno(DeleteView):
    model=Alumnos
    def post(self, request, pk,*args,**kwargs):
        object=Alumnos.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('extension:lista_alumno')


   


def about(request):
    post = Post.objects.filter(estado=True,
    categoria=Categoria.objects.get(nombre__iexact='about'))
    return render(request, 'inicio/about.html',{'post':post})








