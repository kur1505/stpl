# Generated by Django 3.1.5 on 2021-02-11 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210211_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='NODE_Number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='STB_Number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='account_no',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bank_account',
        ),
    ]
