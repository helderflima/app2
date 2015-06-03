from django.contrib import admin
from artigos.models import Agencia, Autor, Artigo

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    ordering = ('nome',)


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'pub_date', 'agencia')
    search_fields = ('titulo', 'agencia')
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fields = ('titulo', 'url', 'pub_date', 'autores', 'agencia', 'conteudo')
    prepopulated_fields = {'url': ('titulo',)}
    filter_horizontal = ('autores',)
    raw_id_fields = ('agencia',)


class AgenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
    search_fields = ('nome', 'site')
    ordering = ('nome',)


admin.site.register(Agencia)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Artigo, ArtigoAdmin)