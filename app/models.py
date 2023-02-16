from django.db import models

class Carro(models.Model):
    marca =models.CharField( max_length=50)
    modelo =models.CharField( max_length=50)
    bits = models.BinaryField(max_length = 1000,default = b'x08')
    


    def __str__(self):
        return self.modelo
