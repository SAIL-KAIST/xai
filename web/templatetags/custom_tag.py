from django import template

register = template.Library()

@register.filter(name='sub')
def subtract(value, arg):
    return value - arg

@register.filter(name='mul')
def multiply(value, arg):
    return value*arg
