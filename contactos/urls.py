from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_contacto, name='crear_contacto'),
    path('contactos/contacto/editar/<slug:slug>/', views.editar_contacto, name='editar_contacto'),
    path('contactos/borrar/<slug:slug>/', views.borrar_contacto, name='borrar_contacto'),

]
