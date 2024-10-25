from django.db import models

# Create your models here.

class Vehiculo(models.Model):

    MARCAS = [
        ('Fiat','Fiat'),
        ('Chevrolet','Chevrolet'),
        ('Ford','Ford'),
        ('Toyota','Toyota')
    ]
    
    CATEGORIAS = [
        ('Particular','Particular'),
        ('Transporte','Transporte'),
        ('Carga','Carga')
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateField(null=True)
    fecha_modificacion = models.DateField(null=True)
    
    # class Meta:
    #     verbose_name = _("Vehiculo")
    #     verbose_name_plural = _("Vehiculos")

    def __str__(self):
        return f'{self.marca} {self.modelo}'

    # def get_absolute_url(self):
    #     return reverse("Vehiculo_detail", kwargs={"pk": self.pk})
