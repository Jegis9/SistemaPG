from django.db import models

# Create your models here.

class Emergencias(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

 
    
# mostrar el contenido del insumo 
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.codigo, self.descripcion, self.ubicacion)
    
    