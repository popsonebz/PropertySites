from django.core.urlresolvers import reverse
from django import template
register = template.Library()


@register.simple_tag
def is_active(request, url):
    # Main idea is to check if the url and the current path is a match
    if request.path in reverse(url):
        return "active"
    return ""
