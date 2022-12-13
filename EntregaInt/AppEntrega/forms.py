from django import forms
from AppEntrega.models import *


class crearFormDiscos(forms.Form):
    
    Años = [x for x in range(1930,2022)]
    
    nombre = forms.CharField(max_length=60)
    artista = forms.CharField(max_length=60)
    stock = forms.IntegerField()
    
class crearFormLecciones(forms.Form):
    
    profesor = forms.CharField(max_length=60)
    instrumento = forms.CharField(max_length=60)
    dicta = forms.BooleanField()
    
class crearFormGuitarras(forms.Form):
    
    modelo = forms.CharField(max_length=60)
    precio = forms.IntegerField()


#class formuLecciones(forms.Form):
    
    #profesor = forms.CharField(max_length=60)
    #instrumento = forms.CharField(max_length=60)
    #dicta = forms.BooleanField()