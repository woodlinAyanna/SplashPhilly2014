
from splash_philly import settings
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def google_api_key():
    return settings.GOOGLE_API_KEY