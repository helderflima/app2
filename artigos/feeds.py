__author__ = 'Helder'
from django.contrib.syndication.views import Feed
from artigos.models import Artigo

class ArtigosRss(Feed):
    title = "Últimos artigos do site"
    link = "/"
    description = "Últimos artigos do site de teste do curso de Django do TreinaWeb"

    def items(self):
        return Artigo.objects.all()

    def item_link(self, artigo):
        return "/artigo/%s" % artigo.url

    def item_description(self, artigo):
        return artigo.conteudo


