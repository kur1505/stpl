# Generated by Django 3.1.5 on 2021-02-19 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20210219_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='STB_Number',
            field=models.CharField(max_length=50, null=True, verbose_name='STB'),
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]