# Generated by Django 2.2.6 on 2019-10-13 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20191013_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardNumber',
            field=models.UUIDField(blank=True, default=uuid.uuid4, help_text='Unique Id for this card', primary_key=True, serialize=False),
        ),
    ]