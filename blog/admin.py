#from django.contrib import admin
#from .models import Postear
#admin.site.register(Postear)
#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.

from django.contrib import admin
from .models import Alumnos, Cursos, Boleta

#Registramos nuestras clases principales.
admin.site.register(Cursos)
admin.site.register(Alumnos)
admin.site.register(Boleta)
