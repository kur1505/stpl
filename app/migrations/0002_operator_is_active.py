# Generated by Django 3.1.5 on 2021-02-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
    ]
