# Generated by Django 2.2.6 on 2019-10-13 17:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20191013_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='id',
        ),
        migrations.AddField(
            model_name='card',
            name='cardNumber',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique Id for this card', primary_key=True, serialize=False),
        ),
    ]
