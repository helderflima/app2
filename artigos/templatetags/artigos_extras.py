__author__ = 'Helder'
from django import template
import datetime

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


@register.tag(name="current_time")
def do_current_time(parser, token):
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requer um argumento simples' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])