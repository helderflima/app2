__author__ = 'helderflima'
from django.http import HttpResponse
import datetime

def ola(request):
    return HttpResponse('Olá pessoas!')

def data_atual(request):
    now = datetime.datetime.now()
    html = "<em>Agora é %s.</em>" % now
    return HttpResponse(html)