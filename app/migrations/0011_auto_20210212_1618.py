# Generated by Django 3.1.5 on 2021-02-12 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operator',
            old_name='is_staff',
            new_name='is_operator',
        ),
    ]
