from django.shortcuts import render, get_object_or_404, HttpResponse
from artigos.models import Artigo, Autor, Agencia
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from artigos.forms import FormContato
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


def form_pesquisa(request):
    return render(request,  'search_form.html')


def pesquisa(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        artigos = Artigo.objects.filter(titulo__contains=q) | Artigo.objects.filter(conteudo__contains=q)
        return render(request, 'search_results.html',
            {'artigos': artigos, 'query': q})
    else:
        return render(request, 'search_form.html', {'erro': True})


def contato(request):
    if request.method == "POST":
        form = FormContato(request.POST)
        if form.is_valid():
            email = ['helder.fl@hotmail.com']
            remetente = form.cleaned_data['email']
            assunto = "Contato - " + form.cleaned_data['nome']
            mensagem = "Telefone: " + form.cleaned_data['telefone'] + "<br/>" + form.cleaned_data['mensagem']
            send_mail(assunto, mensagem, remetente, email)

            return render(request, 'contact.html', {"form": FormContato(), "send": True})
    else:
        form = FormContato()

    return render(request, 'contact.html', {
        "form": form
    })