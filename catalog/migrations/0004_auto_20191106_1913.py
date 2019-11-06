# Generated by Django 2.2.6 on 2019-11-06 19:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191106_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular account', primary_key=True, serialize=False),
        ),
    ]