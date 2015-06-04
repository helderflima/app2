from django.shortcuts import render, get_object_or_404
from artigos.models import Artigo, Autor, Agencia
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def index(request, pagina=1):
    paginacao = Paginator(Artigo.objects.all(), 3)
    try:
        resumo = paginacao.page(pagina)
    except PageNotAnInteger:
        resumo = paginacao.page(1)
    except EmptyPage:
        resumo = paginacao.page(paginacao.num_pages)


    return render(request, 'index.html', {
        'artigos': resumo.object_list,
        'paginacao': resumo,
        'page_now': pagina,
    })


def artigo(request, url):
    return render(request, 'detail.html', {
        'artigo': get_object_or_404(Artigo, url=url)
    })


