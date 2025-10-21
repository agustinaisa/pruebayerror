
from django.urls import path, include
from app import views



urlpatterns = [
    path("",views.index, name="index"),
    path("entrevista/",views.Entrevista_view, name="entrevista"),
    path('gracias/', views.entrevista_completa_view, name='entrevista_completa'),
    
]
    