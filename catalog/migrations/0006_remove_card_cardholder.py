# Generated by Django 2.2.6 on 2019-10-13 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20191013_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='cardHolder',
        ),
    ]