from django import template

register = template.Library()

@register.filter()
def diff_cum_var(indexable, i):
    return indexable[i].cum_var - indexable[i-1].cum_var

@register.filter()
def increase_cum_var(indexable, i):
    return indexable[i].cum_var > indexable[i-1].cum_var

@register.filter()
def previous_var(indexable, i):
    return indexable[i-1].var

@register.filter()
def previous_mae(indexable, i):
    return indexable[i-1].mae

@register.filter()
def abs(value):
    if value >= 0:
        return value
    else:
        return -value