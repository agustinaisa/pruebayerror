
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("",views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.entrevista_view, name='entrevista'),
    path('turnos/', views.turnos_view, name='turnos'),
]
    

