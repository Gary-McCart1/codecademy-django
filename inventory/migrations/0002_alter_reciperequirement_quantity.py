# Generated by Django 5.1.6 on 2025-04-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
