from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache 
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from .forms import FormularioLogin, RegistroForm
from django.contrib.auth.models import User

class RegistroUser(CreateView):
    model=User
    template_name='accounts/register.html'
    form_class=RegistroForm
    success_url=reverse_lazy('login')


class Login(FormView):
    template_name = 'accounts/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('extension:perfil')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args,**kwargs):
        if request.user.is_authenticated:
            print("Se ingreso")
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)
             
    
    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)
        

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('accounts/login')