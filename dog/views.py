from django.shortcuts import render
from .models import Dog

# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404, redirect
from .models import Dog, MedicalCard
from .forms import DogForm
from .filters import DogFilter


def alldogs(request):
    dogs = Dog.objects
    return render(request, 'dog/alldogs.html', {'dogs':dogs})

def dog_detail(request, dog_id):
    dogdetail = get_object_or_404(Dog, pk=dog_id)
    card_m = MedicalCard.objects.filter(dog_id=dog_id)
    context = {'dog':dogdetail, 'card_m':card_m}
    return render(request, 'dog/dog_detail.html', context)

def alldog_image(request):
    dogs = Dog.objects.all()
    myFilter = DogFilter(request.GET, queryset=dogs)
    dogs = myFilter.qs
    context = {'dogs':dogs, 'myFilter':myFilter}
    return render(request, 'dog/alldog_image.html', context)

def medicalcards(request):
    cards = MedicalCard.objects.filter(active=True)
    context = {'cards':cards}
    return render(request, 'dog/medicalcards.html', context)

def card_detail(request, medicalcard_id):
    carddetail = get_object_or_404(MedicalCard, pk=medicalcard_id),
    return render(request, 'dog/card_detail.html', {'carddetail':carddetail})
