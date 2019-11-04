# Generated by Django 2.2.6 on 2019-10-15 21:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20191013_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardNumber',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, help_text='Unique Id for this card', primary_key=True, serialize=False),
        ),
    ]