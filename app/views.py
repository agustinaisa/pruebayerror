from django.shortcuts import render, redirect
from django.http import HttpResponse # Opcional: para un mensaje de éxito simple
from app.forms import EntrevistaForm # Importa la clase de formulario que creaste


def index(request):
    return render(request, "index.html")


def Entrevista_view(request):
    """
    Vista para manejar la lógica de la Entrevista Integral de Admisión.
    """
    if request.method == 'POST':
        # 1. Procesamiento de datos (POST request)
        
        # Se instancia el formulario con los datos enviados en la solicitud.
        form = EntrevistaForm(request.POST) 
        
        if form.is_valid():
            # 2. Los datos cumplen con las reglas definidas en forms.py
            
            # Puedes acceder a los datos limpios y validados:
            datos_entrevista = form.cleaned_data
            
            # --- Lógica de Negocio ---
            # Aquí iría el código para guardar estos datos en la base de datos (Modelo)
            # o para enviarlos por correo electrónico.
            
            # Si tienes un Modelo (ModelForm) harías:
            # form.save() 
            
            # Como estás usando forms.Form, si quieres guardarlo,
            # lo haces manualmente:
            # EntrevistaModel.objects.create(**datos_entrevista) 
            
            # 3. Redirección
            # Se recomienda redirigir a una nueva URL para prevenir
            # el doble envío del formulario si el usuario refresca la página.
            return redirect('entrevista_completa') # Debes definir esta URL en urls.py
        
        # Si el formulario NO es válido, el código continúa y renderiza la plantilla
        # de nuevo, pero con el formulario 'ligado' a los datos enviados,
        # mostrando automáticamente los mensajes de error.
        
    else:
        # 1. Mostrar formulario vacío (GET request)
        
        # Se crea una instancia vacía del formulario.
        form = EntrevistaForm()

    # Renderiza la plantilla, pasando el objeto 'form'
    return render(request, 'entrevista.html', {'form': form})

# Opcionalmente, una vista simple para el éxito:
def entrevista_completa_view(request):
    return HttpResponse("¡Gracias! La entrevista ha sido enviada con éxito.")