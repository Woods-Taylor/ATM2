# Generated by Django 2.2.6 on 2019-10-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_card_cardholder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='dateOfIssue',
        ),
        migrations.RemoveField(
            model_name='account',
            name='expiryDate',
        ),
        migrations.AddField(
            model_name='card',
            name='dateOfIssue',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='expiryDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
