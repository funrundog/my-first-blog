from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=25)
    CHOICES = [('male','Male'), ('female','Female')]
    sex = models.CharField(max_length=250, choices=CHOICES, default='male')
    leader = models.BooleanField()
    for_breeding = models.BooleanField()
    neutered = models.BooleanField()
    avaible_for_adoption = models.BooleanField()
    trekkhundreg = models.URLField(blank = True)
    birth_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    body = models.TextField()
    passport_num = models.CharField(max_length=30, blank = True)
    #chip_num = models.CharField(max_length=30, blank = True)
    #chip_num = models.DecimalField(max_digits=20, decimal_places=0, blank = True)
    breeder = models. CharField(max_length=50, default='own breeding')


    class Meta:
            ordering = ['-birth_date',]

    class Harness(models.TextChoices):
        RED = 'RD', _('Red')
        BLUE = 'BL', _('Blue')
        SILVER = 'SL', _('Silver')
        GREEN = 'GR', _('Green')
        YELLOW = 'YL', _('Yellow')

    harness_size = models.CharField(
        max_length=2,
        choices=Harness.choices,
        default=Harness.SILVER,
    )


    def __unicode__(self):
        return self.harness_size

    def summary(self):
        return self.body[:800]
    def birth_date_pretty(self):
        return self.birth_date.strftime('%e %B %Y')
    def birth_date_year(self):
        return self.birth_date.strftime('%y')
    def is_neutered(self):
        return self.neutered.filter(status=1).count()

    def __str__(self):
        return self.name


class Medication(models.Model):
     name = models.CharField(max_length=100, help_text='i.e. Metacam (2 x 1 ml)')
     usage = models.CharField(max_length=200)

     def __str__(self):
        return self.name

class MedicalCard(models.Model):
     diagnosis = models.CharField(max_length=250)
     treatment = models.ManyToManyField(Medication)
     dosage = models.CharField(max_length=100, blank = True)
     duration = models.DurationField(help_text='[DD] [[hh:]mm:]ss')
     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
     datalogger = models.ForeignKey(User, on_delete=models.CASCADE)
     active = models.BooleanField()
     time = models.DateTimeField(default=timezone.now)
     notes = models.TextField(blank = True)
     #vet_report = FileField(upload_to='documents/', max_length=100)

     def __str__(self):
        return "%s %s" % (self.dog.name, self.diagnosis)
''' returns more than one value, dog gives error, add name from Dog class'''
