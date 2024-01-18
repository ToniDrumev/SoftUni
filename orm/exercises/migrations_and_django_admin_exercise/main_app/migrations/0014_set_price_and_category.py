# Generated by Django 4.2.4 on 2023-10-29 20:15

from django.db import migrations


def set_price(apps, schema_editor):
    MULTIPLY_BY = 120

    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()

    for s in smartphones:
        s.price = len(s.brand) * MULTIPLY_BY

    smartphone_model.objects.bulk_update(smartphones, ['price'])


def set_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()

    for s in smartphones:
        if s.price >= 750:
            s.category = 'Expensive'
        else:
            s.category = 'Cheap'

    smartphone_model.objects.bulk_update(smartphones, ['category'])


def set_price_category(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)


def reverse_set_price_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')

    smartphones = smartphone_model.objects.all()

    default_price = smartphone_model._meta.get_field('price').default
    default_category = smartphone_model._meta.get_field('category').default

    for s in smartphones:
        s.price = default_price
        s.category = default_category

    smartphone_model.objects.bulk_update(smartphones, ['price', 'category'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_price_category, reverse_code=reverse_set_price_category)
    ]