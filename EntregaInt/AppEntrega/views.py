from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *
from django.template import RequestContext

# Create your views here.

def inicio(request):
    
    return render(request, "AppEntrega/inicio.html")


def discos(request):
    
    return render(request, "AppEntrega/discos.html")


def guitarras(request):
    
    return render(request, "AppEntrega/guitarras.html")


def lecciones(request):
    
    return render(request, "AppEntrega/lecciones.html")




def formularioLecciones(request):
    
    
    if request.method == "POST":
    
        formulario = crearFormLecciones(request.POST)
    
        print(formulario)
        
        if formulario.is_valid:
            
            informacion = formulario.cleaned_data
            
            leccion = Lecciones(profesor=informacion['profesor'], instrumento=informacion['instrumento'], dicta=informacion['dicta'])
            
            leccion.save()
            
            formulario = crearFormLecciones()
            
            return render(request, "AppEntrega/leccionesformulario.html", {"formulario": formulario}  )
        
        
    else:
        
            formulario = crearFormLecciones()    
        
            return render(request, "AppEntrega/leccionesformulario.html", {"formulario": formulario} )
        
        



def formularioDiscos(request):
    
    
    if request.method == "POST":
    
        formulario2 = crearFormDiscos(request.POST)
    
        print(formulario2)
        
        if formulario2.is_valid:
            
            informacion2 = formulario2.cleaned_data
            
            disco = Discos(nombre=informacion2['nombre'], artista=informacion2['artista'], stock=informacion2['stock'])
            
            disco.save()
            
            formulario2 = crearFormDiscos()
            
            return render(request, "AppEntrega/discosFormulario.html", {"formulario2": formulario2}  )
        
        
    else:
        
            formulario2 = crearFormDiscos()    
        
            return render(request, "AppEntrega/discosFormulario.html", {"formulario2": formulario2} )
        
        



def formularioGuitarras(request):
    
    
    if request.method == "POST":
    
        formulario3 = crearFormGuitarras(request.POST)
    
        print(formulario3)
        
        if formulario3.is_valid:
            
            informacion3 = formulario3.cleaned_data
            
            guitarra = Guitarras(modelo=informacion3['modelo'], precio=informacion3['precio'])
            
            guitarra.save()
            
            formulario3 = crearFormGuitarras()
            
            return render(request, "AppEntrega/guitarrasFormulario.html", {"formulario3": formulario3}  )
        
        
    else:
        
            formulario3 = crearFormGuitarras()    
        
            return render(request, "AppEntrega/guitarrasFormulario.html", {"formulario3": formulario3} )
        

def busquedaDiscos(request):
    
    return render(request, "AppEntrega/busquedaDiscos.html")

def resultadosDiscos(request):
    
    if request.GET["nombre"]:
        
        nombreBusqueda= request.GET["nombre"]
        
        discoResultados= Discos.objects.filter(nombre__icontains=nombreBusqueda)
        
        print(discoResultados)
        
        
        info = {"discoresultados":discoResultados, "nombrebusqueda":nombreBusqueda}
        return render(request, "AppEntrega/resultadosDiscos.html", info)
        
        
        
        
def busquedaGuitarras(request):
    
    return render(request, "AppEntrega/busquedaGuitarras.html")

def resultadosGuitarras(request):
    
    if request.GET["modelo"]:
        
        modeloBusqueda= request.GET["modelo"]
        
        guitarraResultados= Guitarras.objects.filter(modelo__icontains=modeloBusqueda)
        
        print(guitarraResultados)
        
        
        info = {"guitarraresultados":guitarraResultados, "modelobusqueda":modeloBusqueda}
        return render(request, "AppEntrega/resultadosGuitarras.html", info)





def busquedaLecciones(request):
    
    return render(request, "AppEntrega/busquedaLecciones.html")

def resultadosLecciones(request):
    
    if request.GET["instrumento"]:
        
        instrumentoBusqueda= request.GET["instrumento"]
        
        leccionesResultados= Lecciones.objects.filter(instrumento__icontains=instrumentoBusqueda)
        
        print(leccionesResultados)
        
        
        info = {"leccionesresultados":leccionesResultados, "instrumentobusqueda":instrumentoBusqueda}
        return render(request, "AppEntrega/resultadosLecciones.html", info)
















#form = crearFormLecciones(nombre=request.POST["nombre"], artista=request.POST["artista"], dicta= request.POST["dictando"])
        
        #form.sav
        
    #return render(request, 'AppEntrega/leccionesformulario.html')
        
        
        #formulario = crearFormLecciones(request.POST)
        #if formulario.is_valid():

   # else:
    
    
    #    formulario = crearFormLecciones()
    #return render(request, "/AppEntrega/lecciones.html")
    
    
    
    
    
    
    
    
    
    
    
    
    
    #if request.method == "POST":

    #    lecciones= Lecciones(nombre=request.POST["nombre"], artista=request.POST["artista"], dicta= request.POST["dictando"])
        
    #    lecciones.save()
        
    #return render(request, 'AppEntrega/leccionesformulario.html')
        
        

        #miFormulario = Lecciones(request.POST) #aquí mellega toda la información del html

        #print(miFormulario)

        #if miFormulario.is_valid:   #Si pasó la validación de Django 
                
         #   informacion = miFormulario.cleaned_data

          #  leccionesFormulario = Lecciones(nombre=informacion['nombre'], artista=informacion['artista'], dicta=informacion['dicta']) 

           # leccionesFormulario.save()

            #return render(request, "AppEntrega/leccionesformulario.html") #Vuelvo al inicio o a donde quieran

#        else: 

 #        miFormulario = leccionesFormulario() #Formulario vacio para construir el html

  #       return render(request, "AppEntrega/leccionesformulario.html", {"miFormulario":miFormulario})"""""""
        
