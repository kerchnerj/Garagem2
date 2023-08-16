from django.db import models
from garagem.models import Categoria, Marca

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "modelo"