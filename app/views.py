from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse # Opcional: para un mensaje de éxito simple
#from app.forms import EntrevistaForm # Importa la clase de formulario que creaste
from .models import Paciente, EstadoPaciente   # 👈 Esto es fundamental
from .forms import PacienteForm
from app.forms import PacienteForm, EntrevistaForm

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


def turnos_view(request):
    return render(request, 'turnos.html')

def paciente_list(request):
    estados = EstadoPaciente.objects.filter(activo=True)
    pacientes = [estado.paciente for estado in estados]
    return render(request, 'paciente_list.html', {'pacientes': pacientes})

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()
            EstadoPaciente.objects.create(paciente=paciente, activo=True)
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'paciente_form.html', {'form': form})

def paciente_update(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'paciente_form.html', {'form': form})

def paciente_delete(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    estado = get_object_or_404(EstadoPaciente, paciente=paciente)
    if request.method == 'POST':
        estado.activo = False
        estado.save()
        return redirect('paciente_list')
    return render(request, 'paciente_confirm_delete.html', {'paciente': paciente})