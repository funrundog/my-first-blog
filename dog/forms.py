from django.forms import ModelForm
from .models import Dog


class DogForm(ModelForm):
     class Meta:
       model = Dog
       fields = '__all__'

       #fields.widget.attrs.update({'class': 'w3-button'})
       #body.widget.attrs.update(size='40')
