from django.db import models

# Create your models here.

class Lenguaje(models.Model):
    nom_len = models.CharField(max_length=100,verbose_name="Lenguaje")
    
    def __str__(self):
        fila=self.nom_len
        return fila
    
class SO(models.Model):
    nom_so = models.CharField(max_length=100,verbose_name="SO")
    
    def __str__(self):
        fila=self.nom_so
        return fila
    
class Cliente(models.Model):
    nom = models.CharField(max_length=50,verbose_name="Nombre")
    ap = models.CharField(max_length=50,verbose_name="Apellido Paterno")
    am = models.CharField(max_length=50,verbose_name="Apellido Materno",blank=True)
    foto= models.ImageField(upload_to='imagenes/', verbose_name='Foto',null=True)
    lenguaje=models.ForeignKey(Lenguaje, verbose_name="Lenguaje", on_delete=models.CASCADE)
    so=models.ForeignKey(SO, verbose_name="SO", on_delete=models.CASCADE)
    
    def __str__(self):
            fila=str(self.id)+ "-"+self.nom 
            return fila 
    
    def delete(self, using=None, Keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()