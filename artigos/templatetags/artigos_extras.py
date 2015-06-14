__author__ = 'Helder'
from django import template

register = template.Library()


@register.filter(name='autores')
def autores(value):
    "Converter o objeto ManyRelatedManager para string"
    auts = ''
    try:
        for autor in value.all():
            auts = ' ' + str(autor) + ',' + auts
        auts = auts[0:-1]
    except:
        auts = value
    return auts

# register.filter('autores', autores)