from django import template
from django.template.defaultfilters import stringfilter

register= template.Library()
@register.filter(name='spliter')
@stringfilter
def spliter(a, b):
    return a.split(b)