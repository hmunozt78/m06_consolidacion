from django.shortcuts import render
from django.forms import ValidationError
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required 



# Create your views here.
@login_required(login_url='/usuarios/login/')
@permission_required('vehiculo.add_vehiculo', raise_exception=False, login_url='/')
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