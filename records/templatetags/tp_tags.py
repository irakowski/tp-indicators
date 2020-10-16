from django import template

register = template.Library()

@register.filter
def thousands(value):
    """Formats number values with blank space thousand separator"""
    value = float(value)
    return f"{value:,}".replace(',',' ')