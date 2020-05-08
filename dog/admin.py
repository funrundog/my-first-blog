from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Dog)
admin.site.register(MedicalCard)
admin.site.register(Medication)
admin.site.register(Person)
