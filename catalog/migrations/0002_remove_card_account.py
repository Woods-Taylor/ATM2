# Generated by Django 2.2.6 on 2019-10-13 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='account',
        ),
    ]
