# Generated by Django 3.0.5 on 2020-05-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0005_auto_20200507_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalcard',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='medicalcard',
            name='expired_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('messenger', models.URLField(blank=True, help_text='m.me/username')),
                ('status', models.CharField(choices=[('sponsor', 'Sponsor'), ('adopter', 'Adopter'), ('host', 'Host')], max_length=10)),
                ('dog', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dog.Dog')),
            ],
        ),
    ]
