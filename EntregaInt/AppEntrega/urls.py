from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('Guitarras/', guitarras, name = 'guitarras'),
    path('Discos/', discos, name = 'discos'),
    path('Lecciones/', lecciones, name = 'lecciones'),
    path('formuLecciones/', formularioLecciones, name = 'formulariolecciones'),
    path('formuDiscos/', formularioDiscos, name = 'formulariodiscos'),
    path('formuGuitarras/', formularioGuitarras, name = 'formularioguitarras'),
    path('busquedaDiscos/', busquedaDiscos, name = 'busquedadiscos'),
    path('resultadosDiscos/', resultadosDiscos, name = 'resultadosdiscos'),
    path('busquedaGuitarras/', busquedaGuitarras, name = 'busquedaguitarras'),
    path('resultadosGuitarras/', resultadosGuitarras, name = 'resultadosguitarras'),
    path('busquedaLecciones/', busquedaLecciones, name = 'busquedalecciones'),
    path('resultadosLecciones/', resultadosLecciones, name = 'resultadoslecciones'),    
]