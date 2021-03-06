# Generated by Django 3.0.5 on 2020-05-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0003_auto_20200505_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalcard',
            name='duration',
            field=models.DurationField(help_text='[DD] [[hh:]mm:]ss'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='name',
            field=models.CharField(help_text='i.e. Metacam (2 x 1 ml)', max_length=100),
        ),
    ]
