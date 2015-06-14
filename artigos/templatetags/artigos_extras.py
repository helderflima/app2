__author__ = 'Helder'
from django import template
import re
from django.utils.safestring import mark_safe
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


class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')

def add_class(value, css_class):
    string = str(value)
    match = class_re.search(string)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class), match.group(1))
        if not m:
            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                                          string))
    else:
        return mark_safe(string.replace('>', ' class="%s">' % css_class))
    return value

placeholder_re = re.compile(r'(?<=placeholder=["\'])(.*)(?=["\'])')

def add_placeholder(value, placeholder_text):
    string = str(value)
    match = placeholder_re.search(string)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (placeholder_text, placeholder_text,
                                                    placeholder_text, placeholder_text), match.group(1))
        if not m:
            return mark_safe(placeholder_re.sub(match.group(1) + " " + placeholder_text,
                                          string))
    else:
        return mark_safe(string.replace('>', ' placeholder="%s">' % placeholder_text))
    return value

register.filter('add_class', add_class)
register.filter('add_placeholder', add_placeholder)