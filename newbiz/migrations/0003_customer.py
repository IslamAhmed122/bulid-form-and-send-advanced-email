# Generated by Django 3.2.8 on 2021-10-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newbiz', '0002_remove_ourportfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=2000)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='url')),
            ],
        ),
    ]
