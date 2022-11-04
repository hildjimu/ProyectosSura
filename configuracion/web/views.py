from django.shortcuts import render
from web.formularios.formularioMedico import FormularioMedico

# Create your views here.
#render (renderizar) es pintar
def Home(request):
    return render(request,'index.html')

def Medicos(request):
    #debo utilizar la clase de formulario medico
    #creamos entonces un obejto
    formulario=FormularioMedico()
    diccionario={
        "formulario":formulario
    }
    #activar la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=FormularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            print(datos)


    return render(request,'registrosmedicos.html',diccionario)