from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")
    return render(request, "login.html")
    return render(request, "entrevista.html")
    return render(request, "observaciones.html")
    return render(request, "turnos.html")

    