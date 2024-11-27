"""
URL configuration for Agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

from . import views
from contactos.views import lista_contactos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.login_view,name='login'),
    path('registro',views.registro, name='registro'),
    path('cerrar', views.cerrar, name='cerrar'),

    path('',lista_contactos,name='contactos'),
    path('contactos',include('contactos.urls')),
]
