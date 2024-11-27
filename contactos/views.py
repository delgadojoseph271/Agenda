from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ContactoForm
from django.contrib.auth.decorators import login_required

from .models import Contacto

def crear_contacto(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.usuario = request.user
            contacto.save()
            return redirect('contactos')
    else:
        form = ContactoForm()
    return render(request, 'crear_contacto.html', {'form': form})

def detalle_contacto(request, slug):
    contacto = get_object_or_404(Contacto, slug=slug)
    return render(request, 'detalle_contacto.html', {'contacto': contacto})


def lista_contactos(request):
    if not request.user.is_authenticated:
        return redirect('login')

    usuario = request.user
    contactos = usuario.contactos.all()
    return render(request, 'lista_contactos.html', {'contactos': contactos})

@login_required
def editar_contacto(request, slug):
    contacto = get_object_or_404(Contacto, slug=slug, usuario=request.user)

    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contactos')
    else:
        form = ContactoForm(instance=contacto)

    return render(request, 'editar_contacto.html', {'form': form, 'contacto': contacto})

@login_required
def borrar_contacto(request, slug):
    # Obtener el contacto correspondiente al slug
    contacto = get_object_or_404(Contacto, slug=slug, usuario=request.user)

    if request.method == 'POST':  # Para confirmar que la eliminación es por POST
        contacto.delete()
        return redirect('contactos')  # Redirigir a la lista de contactos

    # Si no es POST, se muestra una confirmación
    return render(request, 'confirmar_borrado.html', {'contacto': contacto})