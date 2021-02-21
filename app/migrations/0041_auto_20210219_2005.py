# Generated by Django 3.1.5 on 2021-02-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_auto_20210219_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='address',
            field=models.CharField(max_length=50, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='message_box',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='mobile',
            field=models.CharField(max_length=50, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='request_id',
            field=models.CharField(max_length=50, null=True, verbose_name='Request ID'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='sr_type',
            field=models.CharField(max_length=50, null=True, verbose_name='Service Request Type'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('1', 'Open'), ('2', 'Work in Progress'), ('3', 'Complete'), ('4', 'Closed'), ('5', 'Canceled')], default='1', max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='sub_type',
            field=models.CharField(max_length=50, null=True, verbose_name='Sub Type'),
        ),
    ]