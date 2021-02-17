"""dptoextension URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.extension.views import Inicio 
from apps.usuarios.views import Login, logoutUser, RegistroUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('extension/',include(('apps.extension.urls','extension'))),
    path('', Inicio.as_view(), name='index'),
    path('accounts/login/',Login.as_view(), name='login'),
    path('accounts/registro/', RegistroUser.as_view(), name='register'),
    path('logout',login_required(logoutUser), name='logout'),
    
]
