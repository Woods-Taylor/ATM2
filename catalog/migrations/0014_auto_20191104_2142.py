# Generated by Django 2.2.6 on 2019-11-05 02:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20191104_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='uniqueNum',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, help_text='Unique Id for this account', primary_key=True, serialize=False),
        ),
    ]
