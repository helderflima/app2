# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('titulo', models.CharField(max_length=80, verbose_name='Título:')),
                ('url', models.SlugField(max_length=200, verbose_name='URL', help_text='URL baseada no título.', unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='Data de publicação')),
                ('conteudo', models.TextField(verbose_name='Conteúdo da página')),
                ('agencia', models.ForeignKey(to='artigos.Agencia')),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='artigo',
            name='autores',
            field=models.ManyToManyField(to='artigos.Autor'),
        ),
    ]
