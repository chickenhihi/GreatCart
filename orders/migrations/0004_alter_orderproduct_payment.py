# Generated by Django 4.0.6 on 2022-07-13 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment'),
        ),
    ]