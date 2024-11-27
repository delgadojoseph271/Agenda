from django.shortcuts import redirect,render
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponseRedirect

from django.contrib import messages

from .forms import RegisterForm
from contactos.models import Contacto

def inicio(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    contactos = Contacto.objects.all()

    return render(request, "index.html",{
        'contactos': contactos 
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('contactos')
    if request.method == 'POST':
        username = request.POST.get('username')  # Obtiene el nombre de usuario del formulario
        password = request.POST.get('password')  # Obtiene la contraseña del formulario

        user = authenticate(username=username, password=password)  # Intenta autenticar al usuario
        print(user)
        if user:
            login(request, user)  # Inicia sesión si la autenticación es exitosa
            messages.success(request, 'Bienvenido {}'.format(user.username))  # Mensaje de éxito

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])  # Redirige a la URL especificada
            return redirect('contactos')  # Redirige a la página principal
        else:
            messages.error(request, "Usuarios o contrasena no validos")
    return render(request,'users/login.html') 

def registro(request):
    form = RegisterForm(request.POST or None)  # Crea el formulario, con datos POST si están disponibles
    if request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST' and form.is_valid():
        user = form.save()  # Crea un nuevo usuario si el formulario es válido
        if user:
            messages.success(request, 'Usuario creado exitosamente')  # Mensaje de éxito
            return redirect('login')
    return render(request, 'users/register.html', {
        'form': form  # Renderiza la plantilla de registro con el formulario
    })

def cerrar(request):
    logout(request)
    messages.success(request,"Sesion cerrada exitosamente")
    return redirect('login')
