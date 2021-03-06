from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=25)
    CHOICES = [('male','Male'), ('female','Female')]
    sex = models.CharField(max_length=6, choices=CHOICES, default='male')

    LOC_CHOICES = [('a_pool','A pool'), ('b_pool','B pool'), ('c_pool','C pool'), ('d_pool','D pool'), ('racing','Racing'), ('out','Out')]
    location = models.CharField(max_length=8, choices=LOC_CHOICES, blank = True)
    leader = models.BooleanField()
    for_breeding = models.BooleanField()
    neutered = models.BooleanField()
    avaible_for_adoption = models.BooleanField()
    trekkhundreg = models.URLField(blank = True)
    birth_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    image_medium = ImageSpecField(source='image',
                                     processors=[ResizeToFill(250, 150)],
                                     format='JPEG',
                                     options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG',
                                     options={'quality': 60})
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
     diagnosis = models.CharField(max_length=30)
     diagnosis_long = models.CharField(max_length=250, blank = True)
     treatment = models.ManyToManyField(Medication)
     dosage = models.CharField(max_length=100, blank = True)
     duration = models.DurationField(help_text='[DD] [[hh:]mm:]ss')
     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
     datalogger = models.ForeignKey(User, on_delete=models.CASCADE)
     active = models.BooleanField(default=True)
     time = models.DateTimeField(default=timezone.now)
     expired_date = models.DateTimeField(blank=True, null=True)
     notes = models.TextField(blank = True)


     def expire(self):
         now = timezone.now()
         if self.active == True and self.expired_date > now:
            return self.active.set(False)

     '''def active(self):
        now = timezone.now()
        if self.stanow and now < self.end:
            return True
        return False

     '''
     #vet_report = FileField(upload_to='documents/', max_length=100)

     class Meta:
             ordering = ['-time',]

     def __str__(self):
        return "%s %s" % (self.dog.name, self.diagnosis)
''' returns more than one value, dog gives error, add name from Dog class'''

class Person(models.Model):
     name = models.CharField(max_length=50)
     phone = models.CharField(max_length=50)
     email = models.EmailField(max_length = 254, blank=True)
     messenger = models.URLField(blank=True, help_text="m.me/username")
     PER_CHOICES = [('sponsor','Sponsor'), ('adopter','Adopter'), ('host','Host')]
     status = models.CharField(max_length=10, choices=PER_CHOICES)
     dog = models.ForeignKey(Dog, on_delete=models.CASCADE, blank=True)

     def __str__(self):
        return self.name
