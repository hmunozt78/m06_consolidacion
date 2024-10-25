from django.shortcuts import render
from django.forms import ValidationError
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

def registro(request):
    #return render(request, "vehiculo/registro_vehiculo.html", {})
    if request.method == 'POST':
        # LÓGICA PARA PROCESAR LOS DATOS Y GUARDARLOS
        form = VehiculoForm(request.POST)
        
        if form.is_valid():
            try:
                vehiculo = form.save(commit=False)
                vehiculo.clean() # váldamos que cumpla con las restricciones del modelo
                vehiculo.save() # guardamos los datos del modelo
                messages.success(request, "producto creado correctamente.")
            
            except ValidationError as e:
                messages.error(request, e.messages)
        else:
            messages.error(request, "Error al intentar crear el producto, intente nuevamente.")
        
        return render(request, "vehiculo/registro_vehiculo.html", {"form": VehiculoForm()})
    
    else:
        form = VehiculoForm()
        return render(request, "vehiculo/registro_vehiculo.html", {"form": form})