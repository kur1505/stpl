# Generated by Django 3.1.5 on 2021-02-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20210219_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='STB_Number',
            field=models.CharField(max_length=50, verbose_name='STB'),
        ),
    ]
