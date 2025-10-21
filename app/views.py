from django.shortcuts import render, redirect
from django.http import HttpResponse # Opcional: para un mensaje de éxito simple
from app.forms import EntrevistaForm # Importa la clase de formulario que creaste


def index(request):
    return render(request, "index.html")

def entrevista_view(request):
    if request.method == 'POST':
        form = EntrevistaForm(request.POST)
        if form.is_valid():
            # Guardás o procesás los datos (más adelante)
            return redirect('gracias')  # o a donde quieras
    else:
        form = EntrevistaForm()

    return render(request, 'index.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'dashboard.html 'Credenciales inválidas'})
    return render(request, 'dashboard.html