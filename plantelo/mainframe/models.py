from django.db import models

class Planta(models.Model):
    Nombre_cientifico = models.CharField(max_length=100)
    # Otros campos del modelo Plantas

    # Cambia 'Id' a 'id' aquí
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.Nombre_cientifico