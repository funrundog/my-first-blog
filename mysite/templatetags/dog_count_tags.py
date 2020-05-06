from django import template
from dog.models import Dog

register = template.Library()

@register.simple_tag
def dog_count():
    return Dog.objects.count()
