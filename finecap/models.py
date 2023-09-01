from django.db import models

# Create your models here.
class Stand(models.Model):
    localizacao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.localizacao

class Reserva(models.Model):
    nome_empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    stand = models.OneToOneField(Stand, on_delete=models.CASCADE)
    quitado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome_empresa