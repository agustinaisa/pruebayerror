from django.shortcuts import render, redirect 
# forms.py
from django import forms
# --- OPCIONES REUTILIZABLES ---

# Para campos Sí/No (donde 'si' y 'no' son los valores internos)
SI_NO_CHOICES = [
    ('si', 'Sí'),
    ('no', 'No'),
]

# Para lactancia y destete (Buena/Mala/Con complicaciones)
LACTANCIA_DESTETE_CHOICES = [
    ('Buena', 'Buena'),
    ('Mala', 'Mala'),
    ('Con complicaciones', 'Con complicaciones'),
]

# Para desempeño escolar (Si/No/Tiene dificultad)
DESEMPENO_CHOICES = [
    ('si', 'Sí'),
    ('no', 'No'),
    ('dificultad', 'Tiene dificultad'),
]

# Para CUD (Si/No/En trámite)
CUD_CHOICES = [
    ('si', 'Sí'),
    ('no', 'No'),
    ('en_tramite', 'En trámite'),
]


class EntrevistaForm(forms.Form):
    # ------------------------------------
    # I. DATOS DEL NIÑO
    # ------------------------------------
    # Mapeo de <input type="text" id="nombre" name="nombre">
    nombre = forms.CharField(label='Nombre del Niño', max_length=100)
    apellido = forms.CharField(label='Apellido del niño', max_length=100)
    
    # DNI: Lo tratamos como texto por si incluye puntos o guiones, pero puedes usar IntegerField.
    dni = forms.CharField(label='DNI del niño', max_length=15)
    
    # Mapeo de <input type="date" id="fecha_nacimiento">
    fecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    # ------------------------------------
    # II. DATOS DEL TUTOR
    # ------------------------------------
    # Mapeo de <input type="email" id="email" name="email">
    email = forms.EmailField(label='Email Madre/Padre o Tutor', max_length=100)
    
    # Mapeo de <input type="tel" id="telefono" name="telefono">
    telefono = forms.CharField(label='Teléfono de contacto', max_length=15)
    localidad = forms.CharField(label='Localidad', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=200)

    # ------------------------------------
    # III. PERIODO PERINATAL Y POSTNATAL/POSTPARTO
    # ------------------------------------
    # Mapeo de <textarea id="embarazo" name="embarazo">
    embarazo = forms.CharField(
        label='¿Tuvo algún inconveniente en el embarazo?',
        widget=forms.Textarea(attrs={'rows': 3})
    )
    
    # Mapeo de <select id="parto" name="parto">
    tipo_parto = forms.ChoiceField(
        label='¿Parto normal o cesárea?',
        choices=[('normal', 'Normal'), ('cesarea', 'Cesárea')],
        widget=forms.Select
    )
    
    # Mapeo de <select id="lactancia" name="lactancia">
    lactancia = forms.ChoiceField(
        label='¿Como fue la lactancia?',
        choices=LACTANCIA_DESTETE_CHOICES,
        widget=forms.Select
    )
    
    # Mapeo de <select id="destete" name="destete">
    destete = forms.ChoiceField(
        label='¿Como fue el destete?',
        choices=LACTANCIA_DESTETE_CHOICES,
        widget=forms.Select
    )
    
    # Mapeo de preguntas Sí/No (Sueño, Alimentación, Habla, Esfínteres, Selectividad)
    dormir = forms.ChoiceField(
        label='En cuanto al sueño ¿Duerme bien?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect # Uso RadioSelect para mejor UX en el Si/No
    )
    alimentacion = forms.ChoiceField(
        label='¿Se alimenta bien?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )
    habla = forms.ChoiceField(
        label='¿Habla?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )
    
    # Mapeo de <input type="number" id="fraces" name="fraces">
    primeras_palabras_edad = forms.IntegerField(
        label='¿A que edad dijo sus primeras palabras? (en meses o años, lo que prefieras)',
        min_value=0,
        max_value=10
    )
    
    # Mapeo de <input type="number" id="caminar" name="caminar">
    edad_camino = forms.IntegerField(
        label='¿A que edad caminó? (en meses o años, lo que prefieras)',
        min_value=0,
        max_value=5
    )
    
    # Mapeo de <input type="number" id="sentar" name="sentar">
    edad_sento = forms.IntegerField(
        label='¿A que edad se sentó? (en meses o años, lo que prefieras)',
        min_value=0,
        max_value=5
    )
    
    esfinteres = forms.ChoiceField(
        label='¿Controla esfínteres?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )
    
    # Mapeo de <input type="number" id="pañales" name="pañales">
    edad_dejo_pañales = forms.IntegerField(
        label='¿A que edad dejo los pañales? (en años)',
        min_value=0,
        max_value=5
    )
    
    # Nota: Tu HTML tiene dos campos con name="alimentacion". Los separo aquí:
    selectividad_alimentaria = forms.ChoiceField(
        label='¿Tiene selectividad alimentaria?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )

    # ------------------------------------
    # IV. DESEMPEÑO Y CONTEXTO ESCOLAR
    # ------------------------------------
    
    # Mapeo de campos Si/No/Dificultad
    lee = forms.ChoiceField(
        label='¿Lee?',
        choices=DESEMPENO_CHOICES,
        widget=forms.Select
    )
    escribe = forms.ChoiceField(
        label='¿Escribe?',
        choices=DESEMPENO_CHOICES,
        widget=forms.Select
    )
    clase_atencion = forms.ChoiceField(
        label='¿Presta atención en clase?',
        choices=DESEMPENO_CHOICES,
        widget=forms.Select
    )
    jornada = forms.ChoiceField(
        label='¿Permanece toda la jornada dentro de clase?',
        choices=DESEMPENO_CHOICES,
        widget=forms.Select
    )
    actividad_extraescolar = forms.ChoiceField(
        label='¿Realiza actividades extraescolares?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )
    gusta_jugar = forms.ChoiceField(
        label='¿Le gusta jugar?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )
    
    # Mapeo de <textarea id="jugar" name="jugar">
    a_que_juega = forms.CharField(
        label='¿A qué le gusta jugar?',
        widget=forms.Textarea(attrs={'rows': 2})
    )
    
    # Mapeo de <textarea id="vida" name="vida">
    dia_vida_diaria = forms.CharField(
        label='¿Cómo es un día de su vida diaria?',
        widget=forms.Textarea(attrs={'rows': 2})
    )

    # ------------------------------------
    # V. ANTECEDENTES CLINICOS
    # ------------------------------------
    
    # Mapeo de <select id="medicacion" name="medicacion">
    medicacion = forms.ChoiceField(
        label='¿Toma alguna medicación?',
        choices=SI_NO_CHOICES,
        widget=forms.RadioSelect
    )
    
    # Mapeo de <textarea id="antecedentes" name="antecedentes">
    antecedentes_familiares = forms.CharField(
        label='¿Tiene antecedentes de algún familiar con discapacidad?',
        widget=forms.Textarea(attrs={'rows': 2})
    )
    
    # Mapeo de <select id="cud" name="cud">
    cud = forms.ChoiceField(
        label='¿Actualmente posee CUD?',
        choices=CUD_CHOICES,
        widget=forms.Select
    )