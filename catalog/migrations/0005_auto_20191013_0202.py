# Generated by Django 2.2.6 on 2019-10-13 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20191013_0118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accountHolder',
            new_name='accountName',
        ),
        migrations.RemoveField(
            model_name='card',
            name='accountNotes',
        ),
        migrations.RemoveField(
            model_name='card',
            name='accountNumber',
        ),
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.CharField(max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='cardStatus',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='dateOfIssue',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='expiryDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phoneNumber',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
