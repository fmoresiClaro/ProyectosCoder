# Generated by Django 5.0 on 2023-12-05 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='categoria',
        ),
    ]
