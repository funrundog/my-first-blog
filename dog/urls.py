from django.urls import path
from . import views

urlpatterns = [
   path('dog/', views.alldogs, name='alldogs'),
   path('dog/<int:dog_id>/', views.dog_detail, name="dog_detail"),
   path('', views.alldog_image, name="alldog_image"),
   path('medicalcards/', views.medicalcards, name="medicalcards"),
   path('medicalcards/<int:medicalcard_id>/', views.card_detail, name="card_detail"),

]
