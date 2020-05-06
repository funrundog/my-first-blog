import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class DogFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="birth_date", lookup_expr='gte')
    end_date = DateFilter(field_name="birth_date", lookup_expr='lte')
    body = CharFilter(field_name='body', lookup_expr='icontains')
    class Meta:
        model = Dog
        fields = '__all__'
        exclude = ['image', 'body', 'trekkhundreg']



'''
class TrainerFilter(django_filters.FilterSet):
    price_lt = django_filters.NumberFilter(field_name="prise", lookup_expr='lt')
    direction = django_filters.CharFilter(widgets = SelectMultiple(attrs={'class': 'custom-select'}))
    class Meta:
        model = Profile
        fields = ['group', 'child', 'price_lt']
'''
