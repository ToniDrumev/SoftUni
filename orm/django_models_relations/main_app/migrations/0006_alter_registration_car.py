# Generated by Django 4.2.4 on 2023-11-06 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_car_owner_registration_car_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='car',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='main_app.car'),
        ),
    ]
