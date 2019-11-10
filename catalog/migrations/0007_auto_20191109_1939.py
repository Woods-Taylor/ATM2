# Generated by Django 2.2.6 on 2019-11-10 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20191108_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=22, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('v', 'Valid'), ('e', 'Expired'), ('s', 'Lost/Stolen'), ('b', 'Blocked')], default='m', help_text='Card status', max_length=1),
        ),
        migrations.AddField(
            model_name='card',
            name='transactionHistory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.cardHistory'),
        ),
    ]
