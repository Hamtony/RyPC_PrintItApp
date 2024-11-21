from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm  # Crearemos el formulario en breve
from django.contrib.auth.decorators import login_required
from .forms import SolicitudEncargoForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.tipo_usuario = form.cleaned_data['tipo_usuario']
            usuario.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def solicitar_encargo(request):
    if request.method == 'POST':
        form = SolicitudEncargoForm(request.POST, request.FILES)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = request.user
            solicitud.estado_id = 1
            solicitud.save()
            print(f"Archivo guardado en: {solicitud.archivo_stl.path}")  # Agregar esta línea
            messages.success(request, "¡Solicitud de impresión enviada con éxito!")
            return redirect('inicio')
    else:
        form = SolicitudEncargoForm()
    return render(request, 'solicitar_encargo.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(request, username=email, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')

def landing_page(request):
    return render(request, 'landing_page.html')