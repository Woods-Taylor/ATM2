# Generated by Django 2.2.6 on 2019-10-13 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_card_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='accountHolder',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]