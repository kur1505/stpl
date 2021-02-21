# Generated by Django 3.1.5 on 2021-02-19 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_auto_20210219_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='address',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='city',
            field=models.CharField(max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='stb',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.stb'),
        ),
    ]