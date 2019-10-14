# Generated by Django 2.2.6 on 2019-10-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20191013_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='cardStatus',
        ),
        migrations.AddField(
            model_name='card',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('v', 'Valid'), ('e', 'Expired'), ('s', 'Lost/Stolen')], default='m', help_text='CARD_Status', max_length=1),
        ),
    ]
