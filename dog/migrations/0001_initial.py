# Generated by Django 3.0.5 on 2020-04-29 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=250)),
                ('leader', models.BooleanField()),
                ('for_breeding', models.BooleanField()),
                ('neutered', models.BooleanField()),
                ('avaible_for_adoption', models.BooleanField()),
                ('trekkhundreg_id', models.URLField(blank=True)),
                ('birth_date', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('body', models.TextField()),
                ('passport_num', models.CharField(blank=True, max_length=30)),
                ('breeder', models.CharField(default='own breeding', max_length=50)),
                ('harness_size', models.CharField(choices=[('RD', 'Red'), ('BL', 'Blue'), ('SL', 'Silver'), ('GR', 'Green'), ('YL', 'Yellow')], default='SL', max_length=2)),
            ],
            options={
                'ordering': ['-birth_date'],
            },
        ),
    ]
