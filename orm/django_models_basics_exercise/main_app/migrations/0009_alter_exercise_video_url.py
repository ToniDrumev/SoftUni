# Generated by Django 4.2.4 on 2023-10-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='video_url',
            field=models.URLField(null=True),
        ),
    ]