# Generated by Django 3.1.5 on 2021-02-20 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_auto_20210219_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='SR_No',
        ),
    ]
