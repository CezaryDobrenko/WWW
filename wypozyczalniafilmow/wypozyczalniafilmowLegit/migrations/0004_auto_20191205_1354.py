# Generated by Django 2.2.7 on 2019-12-05 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalniafilmowLegit', '0003_auto_20191205_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient',
            name='Tworca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Klient', to=settings.AUTH_USER_MODEL),
        ),
    ]
