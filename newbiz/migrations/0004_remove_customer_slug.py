# Generated by Django 3.2.8 on 2021-11-02 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newbiz', '0003_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
    ]