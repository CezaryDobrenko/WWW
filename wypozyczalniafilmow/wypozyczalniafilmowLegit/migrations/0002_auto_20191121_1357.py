# Generated by Django 2.2.7 on 2019-11-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalniafilmowLegit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klient',
            old_name='Misasto',
            new_name='Miasto',
        ),
    ]
