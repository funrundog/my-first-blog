# Generated by Django 3.0.5 on 2020-05-05 19:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=250)),
                ('dosage', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('active', models.BooleanField()),
                ('time', models.DateTimeField(default=datetime.date.today)),
                ('notes', models.TextField()),
                ('datalogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dog.Dog')),
                ('treatment', models.ManyToManyField(to='dog.Medication')),
            ],
        ),
    ]
