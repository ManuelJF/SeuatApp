from django.contrib import admin
from .models import Matricula,Materia,Grupo,Grado,Alumno,Carrera
# Register your models here.

class MatriculaAdmin(admin.ModelAdmin):
    fields = ('clave',)
    list_display = ('clave',)

class AlumnoAdmin(admin.ModelAdmin):
    fields = ('user','matricula','grado','grupo')
    list_display = ('user','matricula','grado','grupo')

class CarreraAdmin(admin.ModelAdmin):
    fields = ('nombre','tipo','materia','alumno')
    list_display = ('nombre','tipo','materia','alumno')


class MateriaAdmin(admin.ModelAdmin):
    fields = ('clave','nombre')
    list_display = ('clave','nombre')


admin.site.register(Matricula,MatriculaAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Materia,MateriaAdmin)
admin.site.register(Grado)
admin.site.register(Grupo)
