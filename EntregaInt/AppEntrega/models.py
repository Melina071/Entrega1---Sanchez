from django.db import models

# Create your models here.

class Discos(models.Model):
    
    def __str__(self):
        
        return f"Nombre: {self.nombre}  ---  Artista: {self.artista}"
    
    nombre = models.CharField(max_length=60)
    artista = models.CharField(max_length=60)
    stock = models.IntegerField()
    
class Guitarras(models.Model):
    
    def __str__(self):
        
        return f'Modelo: {self.modelo} --- Precio: {self.precio}'
    
    modelo = models.CharField(max_length=60)
    precio = models.IntegerField()
    

class Lecciones(models.Model):
    
    def __str__(self):
        
        return f'Profesor: {self.profesor} --- Instrumento: {self.instrumento}'
    
    profesor = models.CharField(max_length=60)
    instrumento = models.CharField(max_length=60)
    dicta = models.BooleanField(default=False)
    #dicta = models.BooleanField(default=False)

