# Generated by Django 2.2.6 on 2019-11-05 01:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20191104_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='uniqueNum',
            field=models.UUIDField(blank=True, default=uuid.uuid1, editable=False, help_text='Unique Id for this account', primary_key=True, serialize=False),
        ),
    ]