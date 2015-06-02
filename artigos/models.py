from django.db import models
from django.db.models import permalink

# Create your models here.


class Agencia(models.Model):
    nome = models.CharField(max_length=50)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()


class Artigo(models.Model):
    titulo = models.CharField('Título:', max_length=80)
    url = models.SlugField(
            'URL',
            max_length=
    )