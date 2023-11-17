# Generated by Django 4.2.4 on 2023-11-15 20:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0, message='The rating must be between 0.0 and 10.0'), django.core.validators.MaxValueValidator(10.0, message='The rating must be between 0.0 and 10.0')]),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='release_year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1990, message='The release year must be between 1990 and 2023'), django.core.validators.MaxValueValidator(2023, message='The release year must be between 1990 and 2023')]),
        ),
    ]
