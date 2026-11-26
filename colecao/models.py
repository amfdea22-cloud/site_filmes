from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    ano = models.IntegerField()
    assistido = models.BooleanField(default=False)
    genero = models.ForeignKey(
        Genero, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.titulo
