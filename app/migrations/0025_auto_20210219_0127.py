# Generated by Django 3.1.5 on 2021-02-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20210219_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]