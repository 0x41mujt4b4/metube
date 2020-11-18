from django import template
import humanfriendly as hf

register = template.Library()

@register.filter()
def readable_size(value, suffix='B'):
    return hf.format_size(value, binary=True)
