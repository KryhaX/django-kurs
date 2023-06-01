# Generated by Django 4.2 on 2023-04-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0002_film_rok_alter_film_tytul'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='film',
            name='opis',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='film',
            name='plakat',
            field=models.ImageField(blank=True, null=True, upload_to='plakaty'),
        ),
        migrations.AddField(
            model_name='film',
            name='premiera',
            field=models.DateField(blank=True, null=True),
        ),
    ]