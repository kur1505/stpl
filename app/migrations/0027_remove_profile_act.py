# Generated by Django 3.1.5 on 2021-02-18 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20210219_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='act',
        ),
    ]
