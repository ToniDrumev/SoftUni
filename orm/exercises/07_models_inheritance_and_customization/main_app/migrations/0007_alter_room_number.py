# Generated by Django 4.2.4 on 2023-11-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
