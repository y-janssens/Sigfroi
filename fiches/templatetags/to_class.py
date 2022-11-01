from django import template
import re

register = template.Library()

@register.filter(name="to_class")
def to_class(value):
    return re.sub(r'[^a-zA-Z0-9]', '', value)