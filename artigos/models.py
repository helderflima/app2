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

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField('Título:', max_length=80)
    url = models.SlugField(
        'URL',
        max_length=200,
        help_text='URL baseada no título.',
        unique=True)
    pub_date = models.DateTimeField('Data de publicação')
    conteudo = models.TextField('Conteúdo da página')
    autores = models.ManyToManyField(Autor)
    agencia = models.ForeignKey(Agencia)
