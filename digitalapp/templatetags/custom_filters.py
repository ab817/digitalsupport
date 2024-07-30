import re
from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def truncate_chars(value, max_length):
    # Strip HTML tags
    value = strip_tags(value)
    if len(value) > max_length:
        return value[:max_length] + '...'
    return value
