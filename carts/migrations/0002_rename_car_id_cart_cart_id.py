# Generated by Django 4.0.4 on 2022-06-06 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='car_id',
            new_name='cart_id',
        ),
    ]
